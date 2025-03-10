import { Component } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import {UserService} from "../../services/user.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css'],
})
export class UserRegisterComponent {
  user = {
    name: '',
    email: '',
    password: '',
    role: 'JOB_SEEKER', // Or 'EMPLOYER'
  };

  constructor(private userService: UserService,
              private router:Router) {}

  onSubmit() {
    this.userService.registerUser(this.user).subscribe((response) => {
       this.router.navigate(['/login']);
      console.log('User registered successfully!', response);
    });
  }



}
