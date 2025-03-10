import {Component, OnInit, ViewChild} from '@angular/core';
import {initFlowbite} from "flowbite";
import {SideBarComponent} from "./components/side-bar/side-bar.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  ngOnInit() {
    initFlowbite();
  }

  @ViewChild(SideBarComponent) sidebarRef!: SideBarComponent;
  sidebarOpen = true;
  // Parent component reacts to sidebar toggle
  onSidebarToggle(isOpen: boolean) {
    console.log('Sidebar is now:', isOpen ? 'Open' : 'Closed');
  }
  title = 'cvRankerFront';
}
