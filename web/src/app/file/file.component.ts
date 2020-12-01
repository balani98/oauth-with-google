import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ConnectionService } from './connection.service';

@Component({
  selector: 'app-file',
  templateUrl: './file.component.html',
  styleUrls: ['./file.component.scss'],
 
})
export class FileComponent implements OnInit {
 
 filename:string
  constructor(private router:Router,private route:ActivatedRoute,private _service:ConnectionService) { 
    this.filename=this.router.getCurrentNavigation().extras.state.example; 
  }
  path :string="C:\\Users\\deepanshu.balani\\Desktop\\part 2 A\\flask-api\\api\\static\\"
  ngOnInit(): void {
  
  
  }

}
