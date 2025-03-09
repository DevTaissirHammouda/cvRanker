package cvrankerback.job;

import java.util.List;

public interface JobService {
    Job postJob(Job job);
    List<Job> getJobsByEmployer(String userEmail);
    List<Job> getAllJobs();
}
