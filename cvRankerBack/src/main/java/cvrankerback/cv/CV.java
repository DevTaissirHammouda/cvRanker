package cvrankerback.cv;


import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.CompoundIndex;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Document(collection = "cvs")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@CompoundIndex(def = "{'jobId': 1, 'jobSeekerId': 1}", unique = true)
public class CV {
    @Id
    private String id;
    @Indexed
    private String jobSeekerId; // Job Seeker User ID
    @Indexed
    private String jobId; // Job ID
    private String fileName;
    private String fileType;
    private byte[] fileData;
    private LocalDateTime createdAt;

}
