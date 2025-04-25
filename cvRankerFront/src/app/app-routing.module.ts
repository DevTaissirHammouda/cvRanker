import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {UserLoginComponent} from "./components/user-login/user-login.component";
import {JobPostingComponent} from "./components/job-posting/job-posting.component";
import {tokenGuard} from "./guard/token-guard.guard";
import {UserRegisterComponent} from "./components/user-register/user-register.component";
import {JobsTableComponent} from "./components/jobs-table/jobs-table.component";
import {AllJobsTableComponent} from "./components/all-jobs-table/all-jobs-table.component";
import {HomeComponent} from "./components/home/home.component";
import {AccountComponent} from "./components/account/account.component";
import {CvsTableComponent} from "./components/cvs-table/cvs-table.component";
import {MyCvComponent} from "./components/my-cv/my-cv.component";


const routes: Routes = [
  { path: '**', redirectTo: 'login' },
  { path: '/', redirectTo: 'login' },

  {
    path: 'home',
    component: HomeComponent,
    canActivate: [],
    children:[


      // { path: 'job', component: JobPostingComponent,canActivate: [tokenGuard] },
      { path: 'jobs', component: JobsTableComponent,canActivate: [tokenGuard] },
      {path: 'jobs/:jobId/:selectedCV', component: CvsTableComponent,canActivate: [tokenGuard]},
      { path: 'allJobs', component: AllJobsTableComponent,canActivate: [tokenGuard] },
      { path: 'myCv', component: MyCvComponent,canActivate: [tokenGuard] },


    ],
  },


  {
    path: 'account',
    component: AccountComponent,
    canActivate: [],
    children:[

      { path: 'login', component: UserLoginComponent },
      { path: 'register', component: UserRegisterComponent },
      { path: '', redirectTo: 'login', pathMatch: 'full' }, // Default route

      { path: '**', redirectTo: 'login' },

    ],


  },

];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
