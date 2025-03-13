import {Component, OnInit} from '@angular/core';
import {BehaviorSubject, combineLatest} from "rxjs";
import {FormControl} from "@angular/forms";
import {JobService} from "../../services/job.service";
import {JobTableService} from "../../servicesTables/job-table.service";
import {initFlowbite} from "flowbite";
import {CvService} from "../../services/cv.service";
import {Router} from "@angular/router";
import {CvTableService} from "../../servicesTables/cv-table.service";

@Component({
  selector: 'app-cvs-table',
  templateUrl: './cvs-table.component.html',
  styleUrl: './cvs-table.component.css'
})
export class CvsTableComponent implements OnInit {
  tableDataSource$ = new BehaviorSubject<any[]>([]);

  displayedColumns$ = new BehaviorSubject<string[]>([
    "jobseekerName",
    "fileName",
    "createdAt",
    'Action'
  ]);
  currentPage$ = new BehaviorSubject<number>(1);
  pageSize$ = new BehaviorSubject<number>(10);
  dataSize=0;
  dataOnPage$ = new BehaviorSubject<any[]>([]);
  searchFormControl = new FormControl();
  sortKey$ = new BehaviorSubject<string>('name');
  sortDirection$ = new BehaviorSubject<string>('asc');



  constructor(
    private cvService:CvService,
    private cvTableservice:CvTableService,
    private router:Router

  ) { }





  //

  ngOnInit() {
    initFlowbite()

    this.loadCvs()
    // table base functions
    // data size
    this.cvTableservice.getCvs().subscribe(changedHeroData => {
      this.tableDataSource$.subscribe(data=>{
        this.dataSize=data.length
      })
    });

    // pagination
    combineLatest(this.tableDataSource$, this.currentPage$, this.pageSize$)
      .subscribe(([allSources, currentPage, pageSize]) => {
        const startingIndex = (currentPage - 1) * pageSize;
        const onPage = allSources.slice(startingIndex, startingIndex + pageSize);
        this.dataOnPage$.next(onPage);
      });



    // Search and sort
    combineLatest(this.cvTableservice.getCvs(), this.searchFormControl.valueChanges, this.sortKey$, this.sortDirection$)
      .subscribe(([changedHeroData, searchTerm, sortKey, sortDirection]) => {




        const heroesArray = Object.values(changedHeroData);
        let filteredHeroes: any[];
        if (!searchTerm) {
          filteredHeroes = heroesArray;
        } else {
          const filteredResults = heroesArray.filter(hero => {
            return Object.values(hero)
              .reduce((prev, curr) => {
                return prev || curr?.toString().toLowerCase().includes(searchTerm.toLowerCase());
              }, false);
          });
          filteredHeroes = filteredResults;
        }
        // filteredHeroes=filteredHeroes.filter(user => user.isArchived==false);

        const sortedHeroes = filteredHeroes.sort((a, b) => {
          if(a[sortKey] > b[sortKey]) return sortDirection === 'asc' ? 1 : -1;
          if(a[sortKey] < b[sortKey]) return sortDirection === 'asc' ? -1 : 1;
          return 0;
        });

        this.tableDataSource$.next(sortedHeroes);
      });

    this.searchFormControl.setValue('');
  }
  changeCurrentPage(page: number) {
    this.currentPage$.next(page)
  }



   selectedCV! :string;
  ///// Logic
  loadCvs() {
   let jobId = this.router.url.split('/')[3]

    this.cvService.getCvs(jobId).subscribe((response) => {
      this.selectedCV = this.router.url.split('/')[4]

      this.cvTableservice.setCvs(response, this.selectedCV);


    })
  }

  showDetails(cvId:string){


      if (this.selectedCV == cvId){
        return true
      }

  return false
}
  showDetailHover(){


      if (this.selectedCV != 'none'){
        return false
      }

    return true
  }
downloadCv(cvId:string){
  this.cvService.downloadCV(cvId).subscribe((response) => {
    const url = window.URL.createObjectURL(response);
    window.open(url);
  })
}

  selectCv(cvId: string) {
    let jobId = this.router.url.split('/')[3];

    // Call your service to select the CV
    this.cvService.selectCv(jobId, cvId).subscribe((response) => {
      // Navigate to the new route after a delay
      setTimeout(() => {
        this.router.navigate([`/home/jobs/${jobId}/${cvId}`]).then(() => {
          // Wait until the navigation is complete, then reload the page
          window.location.reload();
        });
      }, 1000);
    });
  }


// In your component.ts file
  formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleString('en-GB', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    }).replace(',', ''); // To remove comma between date and time
  }


}
