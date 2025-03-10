import { Component, OnInit } from '@angular/core';
import {UserService} from "../../services/user.service";

interface MenuItem {
  label: string;
  icon: string;
  route?: string;
  isActive?: boolean;
  role?: Role[];
}
export enum Role {
  JOB_SEEKER = "JOB_SEEKER",
  EMPLOYER = "EMPLOYER"
}

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {
  isExpanded = true;
  menuItems: MenuItem[] = [
    {
      label: "Home",
      icon: "🏠", // Material Icon for Home
      route: "/home/allJobs",
      isActive: true,
      role: [Role.JOB_SEEKER, Role.EMPLOYER]
    },
    {
      label: "Jobs",
      icon: "📁", // Material Icon for Jobs
      route: "/home/jobs",
      role: [Role.EMPLOYER]
    },
    {
      label: "CV",
      icon: "📄", // Material Icon for CV
      route: "/cv",
      role:  [Role.JOB_SEEKER]
    },
    // {
    //   label: "Settings",
    //   icon: "⚙️", // Material Icon for Settings
    //   route: "/settings"
    // }
  ];

  logoutItem: MenuItem[] = [{

  label: "Logout",
  icon: "🚪🚶",
  route: "/logout"

}]
  ngOnInit(): void {
    this.handleResize();
    window.addEventListener("resize", this.handleResize.bind(this));
  }
constructor(private userService: UserService) {
}
  toggleSidebar(): void {
    this.isExpanded = !this.isExpanded;
  }

  setActive(item: MenuItem): void {
    // Set the active item in the menu
    this.menuItems.forEach(m => m.isActive = false);
    item.isActive = true;
  }

  private handleResize(): void {
    if (window.innerWidth < 768) {
      this.isExpanded = false;
    }
  }
logOut(){
    this.userService.logout();
}

  ngOnDestroy(): void {
    window.removeEventListener("resize", this.handleResize.bind(this));
  }
}
