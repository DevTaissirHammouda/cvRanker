package cvrankerback.job;

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

    @Override
    public Job postJob(Job job) {
        if (!userRepository.existsByEmail(job.getPostedBy())) {
            throw new IllegalArgumentException("User not found");
        }
        job.setPostedAt(LocalDateTime.now());
        return jobRepository.save(job);
    }

    @Override
    public List<Job> getJobsByEmployer(String email) {
        if (!userRepository.existsByEmail(email)) {
            throw new IllegalArgumentException("User not found");
        }
        return jobRepository.findByPostedBy(email);
    }

    @Override
    public List<Job> getAllJobs() {
        return jobRepository.findAll();
    }
}