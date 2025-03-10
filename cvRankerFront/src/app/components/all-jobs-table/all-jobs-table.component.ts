import {Component, OnInit} from '@angular/core';
import {BehaviorSubject, combineLatest} from "rxjs";
import {FormControl} from "@angular/forms";
import {JobService} from "../../services/job.service";
import {JobTableService} from "../../servicesTables/job-table.service";
import {initFlowbite} from "flowbite";

@Component({
  selector: 'app-all-jobs-table',
  templateUrl: './all-jobs-table.component.html',
  styleUrl: './all-jobs-table.component.css'
})
export class AllJobsTableComponent implements OnInit {
  tableDataSource$ = new BehaviorSubject<any[]>([]);

  displayedColumns$ = new BehaviorSubject<string[]>([
    "title",
    "description",
    "postedBy",
    "companyName",
    "postedAt",
    "cvsCount",

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
    private jobService:JobService,
    private jobTableservice:JobTableService

  ) { }





  //

  ngOnInit() {
    initFlowbite()

    this.loadJobs()
    // table base functions
    // data size
    this.jobTableservice.getJobs().subscribe(changedHeroData => {
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
    combineLatest(this.jobTableservice.getJobs(), this.searchFormControl.valueChanges, this.sortKey$, this.sortDirection$)
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

  adjustSort(key: string) {
    if (this.sortKey$.value === key) {
      if (this.sortDirection$.value === 'asc') {
        this.sortDirection$.next('desc');
      } else {
        this.sortDirection$.next('asc');
      }
      return;
    }

    this.sortKey$.next(key);
    this.sortDirection$.next('asc');
  }

  changeStatusFilter(){
    this.currentPage$.next(1)

  }

  changePageSize$(nbPage:number){
    this.pageSize$.next(nbPage)
    this.changeCurrentPage(1)
  }


  ///// Logic
  loadJobs() {
    this.jobService.getJobs().subscribe((response) => {
      this.jobTableservice.setJobs(response)
      console.log(response)
    })
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


  getRowColor( index: number): string {
    // Example condition: alternate row colors based on index
    return index % 2 === 0 ? 'bg-white' : 'bg-gray-100';
  }
}
