
# StudyMate AI Flask Rest Api.


#
## Description

This is the Flask RESTful API for the AI part of the StudyMate app backend. The API provides three routes for summarizing a given pdf file, generating flashcards, and generating a quiz based on a given plain text.

## API Reference

#### 🏠 Home 

```http
  GET /
```


#### 📕 Post A New Summary

```http
  POST /generatesummary
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `auth`      | `string` | **"*"**. internal key for verifying the request |
| `file`  | `string` | **"*"**. the file to generate the summary from  |
| `fileName`  | `string` | **"*"**. name of the file  |
| `lang`  | `string` | **"*"**. lang of the file  |
| `tire`  | `string` | **"*"**. tire of the final user  |



#### 🃟 Post A New flashcards

```http
  POST /generateflashcards
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `auth`      | `string` | **"*"**. internal key for verifying the request |
| `longText`  | `string` | **"*"**. the plain text to generate flashcards from|
| `lang`  | `string` | **"*"**. name of the file  |
| `tire`  | `string` | **"*"**. tire of the final user  |


#### 🤔 Post A New quiz

```http
  POST /generatequiz
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `auth`      | `string` | **"*"**. internal key for verifying the request |
| `longText`  | `string` | **"*"**. the plain text to generate flashcards from|
| `lang`  | `string` | **"*"**. name of the file  |
| `tire`  | `string` | **"*"**. tire of the final user  |


## 💻 Tech Stack

⦿  **Flask**

⦿ **Tiktoken Library**

⦿ **Pdf2 pdfplumber**

⦿ **Openai GPT3.5 API**





## 👤 Author
🌟 Sidi .A Houd 
- [@Github](https://www.github.com/octokatherine)
- [@Linkedin](https://www.linkedin.com/in/sidahmedsaleck/)


