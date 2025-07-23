import {Component, EventEmitter, Input, numberAttribute, OnInit, Output} from '@angular/core';
import {NgForOf, NgIf, NgClass} from "@angular/common";


@Component({
  selector: 'app-pagination',
  standalone: true,
  imports: [
    NgIf,
    NgForOf,
    NgClass,
  ],
  templateUrl: './pagination.component.html',
  styleUrl: './pagination.component.scss'
})


export class PaginationComponent implements OnInit {
  // Make Math available in the template
  Math = Math;
  
  @Output() pageSizeChange = new EventEmitter<number>();

  @Input() collectionSize: number = 1;
  @Input() pageSize: number = 1;
  @Output() pageChange: any= new EventEmitter<number>();
  @Input() currentPage: number = 1;


  ngOnInit(): void {
    this.pageChange.emit(this.currentPage)
  }

  nextPage(): void {
    if (this.currentPage < (this.collectionSize / this.pageSize)) {
      this.currentPage++
      this.pageChange.emit(this.currentPage)
    }
  }

  lastPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--
      this.callPageChange()

    }
  }

  setPage(page: number): void {
    this.currentPage = page;
    this.callPageChange()

  }

  removeComma(n: number) {
    const afterComma = n % 1
    n = n - afterComma + (afterComma > 0 ? 1 : 0)
    return n
  }

  callPageChange() {
    this.pageChange.emit(this.currentPage)
  }

  /**
   * Handles page size change from the dropdown
   */
  onPageSizeChange(event: Event) {
    const selectElement = event.target as HTMLSelectElement;
    const newPageSize = parseInt(selectElement.value, 10);
    
    // Update page size
    this.pageSize = newPageSize;
    
    // Reset to first page when changing page size
    this.currentPage = 1;
    
    // Emit both events
    this.pageSizeChange.emit(newPageSize);
    this.callPageChange();
  }
}
