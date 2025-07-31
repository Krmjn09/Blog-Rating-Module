import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BlogService } from '../../services/blog.service';
import { Blog } from '../../models/blog.model';

@Component({
  selector: 'app-blog-detail',
  standalone: true,
  imports: [CommonModule],
  providers: [BlogService],
  templateUrl: './blog-detail.html',
  styleUrls: ['./blog-detail.scss']
})
export class BlogDetail implements OnInit {
  blogId!: number;
  blog: Blog | null = null;

  constructor(
    private route: ActivatedRoute,
    private blogService: BlogService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.blogId = +params['id'];
      this.fetchBlog();
    });
  }

  fetchBlog(): void {
    this.blogService.getBlog(this.blogId).subscribe({
      next: (data) => this.blog = data,
      error: (err) => {
        console.error('Failed to fetch blog', err);
        alert('Failed to load blog.');
      }
    });
  }
}
