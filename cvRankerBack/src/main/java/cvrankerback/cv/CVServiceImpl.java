package cvrankerback.cv;

import cvrankerback.job.Job;
import cvrankerback.job.JobRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
@RequiredArgsConstructor
public class CVServiceImpl implements CVService {
    private final CVRepository cvRepository;

    @Override
    public CV uploadCV(CV cv) {
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