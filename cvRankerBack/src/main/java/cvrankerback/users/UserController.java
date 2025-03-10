package cvrankerback.users;

import cvrankerback.users.DTO.userRegisterDTO;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {
    private final UserService userService;

    @Operation(summary = "Register a new user", description = "Register a new user with the given user details")

    @PostMapping("/register")
    public ResponseEntity<User> registerUser(@RequestBody userRegisterDTO user) {
        User savedUser = userService.registerUser(user);
        return ResponseEntity.ok(savedUser);
    }

    @Operation(summary = "Login", description = "Login with the given email and password")
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestParam String email, @RequestParam String password) {
        Optional<User> userOptional = userService.login(email, password);

        if (userOptional.isPresent()) {
            User user = userOptional.get();

            // Simulate token (Replace this with real JWT token implementation later)
            String fakeToken = "mock-token-" + user.getId()+ "-" + user.getEmail();

            // Prepare response with token and user role
            Map<String, String> response = new HashMap<>();
            response.put("token", fakeToken);
            response.put("role", String.valueOf(user.getRole()));

            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.status(401).body("Invalid email or password");
        }
    }

    @GetMapping("/find/{email}")

    public ResponseEntity<User> findUserByEmail(@PathVariable String email) {
        return userService.findUserByEmail(email)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }
}
