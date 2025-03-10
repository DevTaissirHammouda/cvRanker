import { Component, OnInit } from '@angular/core';

interface MenuItem {
  label: string;
  icon: string;
  route?: string;
  isActive?: boolean;
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
      route: "/home",
      isActive: true
    },
    {
      label: "Jobs",
      icon: "📁", // Material Icon for Jobs
      route: "/jobs",
    },
    {
      label: "CV",
      icon: "📄", // Material Icon for CV
      route: "/cv",
    },
    {
      label: "Settings",
      icon: "⚙️", // Material Icon for Settings
      route: "/settings"
    }
  ];

  ngOnInit(): void {
    this.handleResize();
    window.addEventListener("resize", this.handleResize.bind(this));
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

  ngOnDestroy(): void {
    window.removeEventListener("resize", this.handleResize.bind(this));
  }
}
