package cvrankerback.cv;

import cvrankerback.cv.DTO.CVsDto;
import cvrankerback.job.Job;
import cvrankerback.job.JobRepository;
import cvrankerback.users.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
@RequiredArgsConstructor
public class CVServiceImpl implements CVService {
    private final CVRepository cvRepository;
    private final JobRepository jobRepository;
    private final UserRepository userRepository;

    @Override
    public CV uploadCV(CV cv) {
        if (!jobRepository.existsById(cv.getJobId())) {
            throw new IllegalArgumentException("Job not found");
        }
        if (!userRepository.existsById(cv.getJobSeekerId())) {
            throw new IllegalArgumentException("Job Seeker not found");
        }
        return cvRepository.save(cv);
    }

    @Override
    public List<CVsDto> getCVsByJob(String jobId) {


        List<CV> cvs= cvRepository.findByJobId(jobId);
        List<CVsDto> cvsDtos = cvs.stream().map(cv -> {
            String jobSeekerName = userRepository.findById(cv.getJobSeekerId()).get().getName();
            return new CVsDto(cv.getId(),jobSeekerName, cv.getFileName(),  cv.getCreatedAt());
        }).toList();
        return cvsDtos;
    }

    @Override
    public List<CV> getCVsByJobSeeker(String jobSeekerId) {
        return cvRepository.findByJobSeekerId(jobSeekerId);
    }

    @Override
    public ResponseEntity<?> selectCV(String jobId, String cvId) {
        Job job = jobRepository.findById(jobId).orElseThrow(() -> new IllegalArgumentException("Job not found"));
        job.setSelectedCV(cvId);
        jobRepository.save(job);
        return ResponseEntity.ok().build();
    }
}
