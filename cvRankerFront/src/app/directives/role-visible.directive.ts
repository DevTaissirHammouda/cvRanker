import { Directive, Input, ElementRef, Renderer2, OnInit } from '@angular/core';
import {Role} from "../components/side-bar/side-bar.component";

@Directive({
  selector: '[appRoleVisible]'
})
export class RoleVisibleDirective implements OnInit {
  @Input() appRoleVisible: Role | Role[] | undefined; // The role(s) for which the element should be visible

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  ngOnInit(): void {
    const userRole = this.getUserRoleFromLocalStorage(); // Get role from localStorage

    // If no role is found in localStorage, hide the element
    if (!userRole) {
      this.renderer.setStyle(this.el.nativeElement, 'display', 'none');
      return;
    }

    // Check if the user's role matches the provided role(s)
    if (!this.appRoleVisible) {
      // If no role is provided, show the element by default
      this.renderer.setStyle(this.el.nativeElement, 'display', 'block');
      return;
    }

    // If role is an array, check if the user's role is included
    if (Array.isArray(this.appRoleVisible)) {
      if (this.appRoleVisible.includes(userRole)) {
        this.renderer.setStyle(this.el.nativeElement, 'display', 'block');
      } else {
        this.renderer.setStyle(this.el.nativeElement, 'display', 'none');
      }
    } else {
      // If it's a single role, compare directly
      if (this.appRoleVisible === userRole) {
        this.renderer.setStyle(this.el.nativeElement, 'display', 'block');
      } else {
        this.renderer.setStyle(this.el.nativeElement, 'display', 'none');
      }
    }
  }

  private getUserRoleFromLocalStorage(): Role | null {
    const role = localStorage.getItem('role'); // Fetch the 'role' key from localStorage

    return role ? <Role>role : null; // Return null if no role found
  }
}
