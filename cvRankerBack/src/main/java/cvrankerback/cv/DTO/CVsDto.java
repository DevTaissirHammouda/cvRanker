package cvrankerback.cv.DTO;

import lombok.Data;

import java.time.LocalDateTime;


@Data
public class CVsDto {
    private String id;
    private String jobseekerName; // Job Seeker name
    private String fileName;
//    private String fileType;
    private LocalDateTime createdAt;
    public CVsDto(String id,String jobseekerName, String fileName, LocalDateTime createdAt) {
        this.id = id;
        this.jobseekerName = jobseekerName;
        this.fileName = fileName;
//        this.fileType = fileType;
//        this.fileData = fileData;
        this.createdAt = createdAt;
    }
}
