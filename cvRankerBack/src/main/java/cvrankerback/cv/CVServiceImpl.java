package cvrankerback.cv;

import cvrankerback.job.Job;
import cvrankerback.job.JobRepository;
import cvrankerback.users.UserRepository;
import lombok.RequiredArgsConstructor;
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
    public List<CV> getCVsByJob(String jobId) {
        return cvRepository.findByJobId(jobId);
    }

    @Override
    public List<CV> getCVsByJobSeeker(String jobSeekerId) {
        return cvRepository.findByJobSeekerId(jobSeekerId);
    }
}