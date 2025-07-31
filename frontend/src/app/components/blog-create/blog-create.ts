import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { BlogService } from '../../services/blog.service';
import { Blog } from '../../models/blog.model';

@Component({
  selector: 'app-blog-create',
  standalone: true,
  imports: [CommonModule, FormsModule],
  providers: [BlogService],
  templateUrl: './blog-create.html',
  styleUrls: ['./blog-create.scss']
})
export class BlogCreate {
  blog: Blog = {
    user_name: '',
    title: '',
    content: '',
    tag: '',
    likes: 0,
    comments: 0,
    rating: 0
  };

  constructor(private blogService: BlogService, private router: Router) {}

  submitBlog(): void {
    this.blogService.createBlog(this.blog).subscribe({
      next: () => {
        alert('Blog created successfully!');
        this.router.navigate(['/']);
      },
      error: (err) => {
        console.error('Failed to create blog', err);
        alert('Failed to create blog.');
      }
    });
  }
}
