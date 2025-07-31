import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { BlogService } from '../../services/blog.service';
import { Blog } from '../../models/blog.model';

@Component({
  selector: 'app-blog-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  providers: [BlogService],  // ✅ Add this line
  templateUrl: './blog-list.html',
  styleUrls: ['./blog-list.scss']
})
export class BlogList implements OnInit {
  blogs: Blog[] = [];

  constructor(private blogService: BlogService) {}

  ngOnInit(): void {
    this.loadBlogs();
  }

  loadBlogs(): void {
    this.blogService.getBlogs().subscribe({
      next: (data) => this.blogs = data,
      error: (err) => console.error('Failed to fetch blogs', err)
    });
  }
}
