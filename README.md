# API-students-portal
A student portal project that acts as an online portal between students and the admin built using GraphQL with Django.


### GraphQL Query

- #### Get all users
```
query {
    users {
        id
        email
        username
        isActive
        isSuperuser
        dateJoined
    }
}
```

- #### Get all courses
```
query {
  courses {
    id
    name
    description
  }
}
```

- #### Get a single course
```
query {
  course(courseId: 1) {
    id
    name
    description
  }
}
```

- #### Get all students
```
query {
    students {
        id
        email
        username
        isActive
        course {
            id
            name
            description
        }
    }
}
```

- #### Get a single student
```
query {
  student(studentId:1) {
    id
    email
    username
    isActive
    course {
      id
      name
      description
    }
  }
}
```

### GraphQL Mutation

- #### Create new course
```
mutation {
    createCourse(name:"Bachelor of Science in Water Resources Engineering", description:"The water resources engineering curriculum is designed to prepare interested students for future careers in water supply, waste water, floodplain, storm water.") {
        course {
          id 
          name
          description
        }
    }
}
```

- #### Create new student
```
mutation {
    createStudent(username:"tomas", email:"tomas@gmail.com", firstName:"dollar", lastName:"tomas", gender:"female", password:"tomas123", courseId:1, isActive: "t") {
        student {
             id 
             username
             email
             firstName
             lastName
             gender
             password
             isActive
             course { 
                id 
                name 
                description
             }
        }
    }
}
```

- #### Update course by id
```
mutation {
    updateCourse(pk:2, name:"Bachelor of Computer Engineering", description:"computer Engineering prepares the graduate for developing and using technologies, as well as being able to design, produce, and manage data elaboration systems in a wide range of applications.") {
        course {
            id 
            name
            description
        }
    }
}
```

- #### Update student by id
```
mutation {
    updateStudent(pk:2, username:"Dominic", email:"ematembu2@gmail.com", firstName: "Manuel", lastName: "Dominic", courseId: 1, gender: "male", isActive: "t") {
        student {
            id 
            username
            email
            firstName
            lastName
            gender
            isActive
        }
    }
}
```

- #### Delete course by id
```
mutation {
    deleteCourse(pk:4) {
        message 
    }
}
```

- #### Delete student by id
```
mutation {
    deleteStudent(pk:3) {
        message 
    }
}
```
