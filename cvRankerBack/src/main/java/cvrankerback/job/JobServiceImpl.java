package cvrankerback.job;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class JobServiceImpl implements JobService {
    private final JobRepository jobRepository;

    @Override
    public Job postJob(Job job) {
        job.setPostedAt(LocalDateTime.now());
        return jobRepository.save(job);
    }

    @Override
    public List<Job> getJobsByEmployer(String employerId) {
        return jobRepository.findByPostedBy(employerId);
    }

    @Override
    public List<Job> getAllJobs() {
        return jobRepository.findAll();
    }
}