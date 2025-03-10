package cvrankerback.job.dto;


import lombok.Builder;
import lombok.Data;

import java.time.LocalDateTime;

@Builder
@Data
public class jobDto {

        private String title;
        private String description;
        private String companyName;
        private String postedBy; // Employer ID
        private LocalDateTime postedAt;
        private Long CVsCount;
        private String id;

        public jobDto(String title, String description, String companyName, String postedBy, LocalDateTime postedAt , Long CVsCount, String id) {

            this.title = title;
            this.description = description;
            this.companyName = companyName;
            this.postedBy = postedBy;
            this.postedAt = postedAt;
            this.CVsCount = CVsCount;
            this.id = id;

        }
}
