package cvrankerback.cv;

import cvrankerback.cv.DTO.CVsDto;
import org.springframework.http.ResponseEntity;

import java.util.List;

public interface CVService {
    CV uploadCV(CV cv);
    List<CVsDto> getCVsByJob(String jobId);
    List<CV> getCVsByJobSeeker(String jobSeekerId);
    ResponseEntity<?> selectCV(String jobId, String cvId);
    CV uploadCVJobSeeker(CV cv);
}
