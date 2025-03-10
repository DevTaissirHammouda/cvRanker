import { Component } from '@angular/core';
import { UserService } from '../../services/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css'], // Fixed `styleUrl` to `styleUrls`
})
export class UserLoginComponent {
  user = {
    email: '',
    password: '',
  };

  errorMessage: string = '';

  constructor(private userService: UserService, private router: Router) {}

  onLogin() {
    this.userService.loginUser(this.user).subscribe(
      (response) => {
        console.log('Login successful!', response);

        if (response && response.token) {
          localStorage.setItem('token', response.token); // Store token
          localStorage.setItem('role', response.role || 'user'); // Default to 'user' if role is undefined
          localStorage.setItem('email', this.user.email); // Store email
          if (response.role === 'JOB_SEEKER') {
          this.router.navigate(['/home/job']);
          }
          if (response.role === 'EMPLOYER') {
          this.router.navigate(['/home/jobs']);

          }
        } else {
          this.errorMessage = 'Invalid response from server.';
        }
      },
      (error) => {
        this.errorMessage = 'Invalid email or password';
        console.error('Login failed:', error);
      }
    );
  }
}
