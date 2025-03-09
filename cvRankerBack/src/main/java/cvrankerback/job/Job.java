package cvrankerback.job;


import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.LocalDateTime;

@Document(collection = "jobs")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Job {
    @Id
    private String id;
    private String title;
    private String description;
    private String companyName;
    private String postedBy; // Employer ID
    private LocalDateTime postedAt;
}