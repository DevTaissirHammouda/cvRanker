package cvrankerback.users;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Getter
@Setter
@ToString
@EqualsAndHashCode
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Document(collection = "users")
public class User {
    @Id
    private String id;
    private String name;
    private String email;
    private String password; // Will be encrypted
    private Role role; // EMPLOYER or JOB_SEEKER
}


enum Role {
    JOB_SEEKER, EMPLOYER
}