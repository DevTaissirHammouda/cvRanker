package cvrankerback.users.DTO;

import cvrankerback.users.Role;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class userRegisterDTO {

    private String name;
    private String email;
    private String password; // Will be encrypted
    private Role  role;

    public userRegisterDTO(String name, String email, String password, Role role) {

        this.name = name;
        this.email = email;
        this.password = password;
        this.role = role;
    }


}
