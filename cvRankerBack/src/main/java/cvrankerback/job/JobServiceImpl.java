package cvrankerback.job;

import cvrankerback.cv.CVRepository;
import cvrankerback.job.dto.jobDto;
import cvrankerback.users.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class JobServiceImpl implements JobService {
    private final JobRepository jobRepository;
    private final UserRepository userRepository;
    private final CVRepository cvRepository;

    @Override
    public Job postJob(Job job) {
        if (!userRepository.existsByEmail(job.getPostedBy())) {
            throw new IllegalArgumentException("User not found");
        }
        job.setPostedAt(LocalDateTime.now());
        return jobRepository.save(job);
    }

    @Override
    public List<jobDto> getJobsByEmployer(String email) {
        if (!userRepository.existsByEmail(email)) {
            throw new IllegalArgumentException("User not found");
        }
        List<Job> jobs = jobRepository.findByPostedBy(email);
        List<jobDto> jobDtos = jobs.stream().map(job -> {
            long cvCount = cvRepository.countByJobId(job.getId());
            return jobDto.builder()
                    .id(job.getId())
                    .title(job.getTitle())
                    .description(job.getDescription())
                    .companyName(job.getCompanyName())
                    .postedBy(job.getPostedBy())
                    .postedAt(job.getPostedAt())
                    .CVsCount(cvCount)
                    .build();
        }).toList();

        return jobDtos;
    }

    @Override
    public List<Job> getAllJobs() {
        return jobRepository.findAll();
    }
}