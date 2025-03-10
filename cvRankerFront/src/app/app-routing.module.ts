import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {UserLoginComponent} from "./components/user-login/user-login.component";
import {JobPostingComponent} from "./components/job-posting/job-posting.component";
import {tokenGuard} from "./guard/token-guard.guard";
import {UserRegisterComponent} from "./components/user-register/user-register.component";
import {JobsTableComponent} from "./components/jobs-table/jobs-table.component";


const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' }, // Default route
  { path: 'login', component: UserLoginComponent },
  { path: 'register', component: UserRegisterComponent },
  { path: 'job', component: JobPostingComponent,canActivate: [tokenGuard] },
  { path: 'jobs', component: JobsTableComponent,canActivate: [tokenGuard] },
  { path: '**', redirectTo: 'login' } // Redirect unknown paths
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
