import { Component, OnInit } from '@angular/core';
import {UserService} from "../../services/user.service";
import {Router} from "@angular/router";

interface MenuItem {
  label: string;
  icon: string;
  route?: string;
  isActive?: boolean;
  role?: Role[];
  isLogout?: boolean;
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
      icon: "fa-solid fa-house",
      route: "/home/allJobs",
      isActive: true,
      role: [Role.JOB_SEEKER, Role.EMPLOYER]
    },
    {
      label: "Jobs",
      icon: "fa-solid fa-folder-open",
      route: "/home/jobs",
      role: [Role.JOB_SEEKER,Role.EMPLOYER]
    },
    {
      label: "My resume",
      icon: "fa-solid fa-file",
      route: "/home/myCv",
      role: [Role.JOB_SEEKER,Role.EMPLOYER]
    },

    {
      label: "Logout",
      icon: "fa-solid fa-arrow-right-from-bracket",
      route: "/logout",
      isLogout: true // Flag for logout action
    }
  ];
  ngOnInit(): void {
    this.handleResize();
    window.addEventListener("resize", this.handleResize.bind(this));
  }
constructor(private userService: UserService,
            private router: Router) {
}
  toggleSidebar(): void {
    this.isExpanded = !this.isExpanded;
  }

  setActive(item: MenuItem) {
    this.menuItems.forEach(menu => menu.isActive = false);
    item.isActive = true;

    if (!item.isLogout) {
      this.router.navigate([item.route]);
    } else {
      this.logOut();
    }
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
