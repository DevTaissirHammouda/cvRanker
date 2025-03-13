import {Component, ElementRef, EventEmitter, Input, OnInit, Output, ViewChild} from '@angular/core';

import {CvService} from "../../../services/cv.service";
import {SharedInformationService} from "../../../servicesTables/shared-information.service";
import {initFlowbite, Modal} from "flowbite";

@Component({
  selector: 'app-cv-post-modal',
  templateUrl: './cv-post-modal.component.html',
  styleUrl: './cv-post-modal.component.css'
})
export class CvPostModalComponent implements OnInit {
  @ViewChild('fileInput') fileInput!: ElementRef;
  @Output() close = new EventEmitter<void>();
  @Output() uploadSuccess = new EventEmitter<any>();


  selectedFile: File | null = null;
  isUploading = false;
  errorMessage = '';
  dragOver = false;

  constructor(
    private cvService: CvService,
    private sharedInformationService: SharedInformationService

  ) {

  }

  onFileSelected(event: any): void {
    const file = event.target.files[0];
    if (file) {
      this.validateFile(file);
    }
  }

  validateFile(file: File): void {
    // Check if the file is a PDF
    if (file.type !== 'application/pdf') {
      this.errorMessage = 'Only PDF files are allowed';
      this.selectedFile = null;
      return;
    }

    // Check file size (5MB max)
    if (file.size > 5 * 1024 * 1024) {
      this.errorMessage = 'File size cannot exceed 5MB';
      this.selectedFile = null;
      return;
    }

    this.selectedFile = file;
    this.errorMessage = '';
  }

  uploadPdf(): void {
    if ( !this.selectedFile ) {
      return;
    }

    this.isUploading = true;
    this.errorMessage = '';
    let jobSeekerEmail = localStorage.getItem('email') ;
    if (!jobSeekerEmail) {
      this.errorMessage = 'An error occurred while uploading the file';
      this.isUploading = false;
      return;
    }
    let jobID = this.sharedInformationService.getJobId();
    console.log(jobID.value);
    const formData = new FormData();
    formData.append('file', this.selectedFile);
    formData.append('jobSeekerEmail', jobSeekerEmail);
    formData.append('jobId', jobID.value.toString());

    this.cvService.uploadCV(formData).subscribe(
      (response) => {
        this.uploadSuccess.emit(response);
        this.isUploading = false;
      },
      (error) => {
        this.errorMessage = 'An error occurred while uploading the file';
        this.isUploading = false;
      }
    );
  }

  browseFiles(): void {
    this.fileInput.nativeElement.click();
  }


  onDragOver(event: DragEvent): void {
    event.preventDefault();
    this.dragOver = true;
  }

  onDragLeave(event: DragEvent): void {
    event.preventDefault();
    this.dragOver = false;
  }

  onDrop(event: DragEvent): void {
    event.preventDefault();
    this.dragOver = false;

    if (event.dataTransfer?.files.length) {
      const file = event.dataTransfer.files[0];
      this.validateFile(file);
    }
  }
  modal: Modal|null = null;
  ngOnInit(): void {



      const $targetEl = document.getElementById('popup-modal-post-cv');

// options with default values
      const options:any = {
        placement: 'center',
        backdrop: 'dynamic',
        backdropClasses:
          'bg-gray-900/50 dark:bg-gray-900/80 fixed inset-0 z-40',
        closable: true,
        onHide: () => {
          // console.log('modal is hidden');
        },
        onShow: () => {
          // console.log('modal is shown');
        },
        onToggle: () => {
          // console.log('modal has been toggled');
        },
      };

// instance options object
      const instanceOptions = {
        id: 'popup-modal-post-cv',
        override: true
      };

      this.modal = new Modal($targetEl, options, instanceOptions);
    }



    showModel() {
      this.modal?.show();
    }



    closeModal() {
    this.selectedFile = null;
      this.modal?.hide();
    }

  }
