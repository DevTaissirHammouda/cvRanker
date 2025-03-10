package cvrankerback.job;

import cvrankerback.job.dto.jobDto;

import java.util.List;

public interface JobService {
    Job postJob(Job job);
    List<jobDto> getJobsByEmployer(String userEmail);
    List<Job> getAllJobs();

}
