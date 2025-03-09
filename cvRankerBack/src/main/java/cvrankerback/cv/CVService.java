package cvrankerback.cv;

import java.util.List;

public interface CVService {
    CV uploadCV(CV cv);
    List<CV> getCVsByJob(String jobId);
    List<CV> getCVsByJobSeeker(String jobSeekerId);
}