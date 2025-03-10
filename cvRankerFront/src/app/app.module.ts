import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserRegisterComponent } from './components/user-register/user-register.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { JobPostingComponent } from './components/job-posting/job-posting.component';
import { UserLoginComponent } from './components/user-login/user-login.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import { JobsTableComponent } from './components/jobs-table/jobs-table.component';
import { CvsTableComponent } from './components/cvs-table/cvs-table.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import {
  CdkCell,
  CdkCellDef, CdkColumnDef,
  CdkHeaderCell,
  CdkHeaderCellDef, CdkHeaderRow,
  CdkHeaderRowDef, CdkRow,
  CdkRowDef,
  CdkTable
} from "@angular/cdk/table";
import {PaginationComponent} from "./components/jobs-table/pagination/pagination.component";
import { SideBarComponent } from './components/side-bar/side-bar.component';
import { RoleVisibleDirective } from './directives/role-visible.directive';
import { AllJobsTableComponent } from './components/all-jobs-table/all-jobs-table.component';

@NgModule({
  declarations: [
    AppComponent,
    UserRegisterComponent,
    JobPostingComponent,
    UserLoginComponent,
    JobsTableComponent,
    CvsTableComponent,
    SideBarComponent,
    RoleVisibleDirective,
    AllJobsTableComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    CdkTable,
    PaginationComponent,
    CdkHeaderRowDef,
    CdkRowDef,
    CdkCellDef,
    CdkHeaderCellDef,
    CdkHeaderCell,
    CdkCell,
    CdkColumnDef,
    CdkRow,
    CdkHeaderRow
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
