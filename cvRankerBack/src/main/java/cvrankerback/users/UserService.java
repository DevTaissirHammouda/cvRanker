package cvrankerback.users;

import cvrankerback.users.DTO.userRegisterDTO;

import java.util.Optional;

public interface UserService {
    User registerUser(userRegisterDTO user);
    Optional<User> login(String email, String password);
    Optional<User> findUserByEmail(String email);
}