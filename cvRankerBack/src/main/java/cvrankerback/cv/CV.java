package cvrankerback.cv;


import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Document(collection = "cvs")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CV {
    @Id
    private String id;
    private String jobSeekerId; // Job Seeker User ID
    private String jobId; // Job ID
    private String fileName;
    private String fileType;
    private byte[] fileData;
    private LocalDateTime createdAt;

}
