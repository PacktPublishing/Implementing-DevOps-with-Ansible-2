# Implementing DevOps with Ansible 2
This is the code repository for [Implementing DevOps with Ansible 2](https://www.packtpub.com/networking-and-servers/implementing-devops-ansible-2?utm_source=github&utm_medium=repository&utm_campaign=9781787120532), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Thinking about adapting the DevOps culture for your organization using a very simple, yet powerful automation tool, Ansible 2? Then this book is for you!

In this book, you will start with the role of Ansible in the DevOps module, which covers fundamental DevOps practices and how Ansible is leveraged by DevOps organizations to implement consistent and simplified configuration management and deployment. You will then move on to the next module, Ansible with DevOps, where you will understand Ansible fundamentals and how Ansible Playbooks can be used for simple configuration management and deployment tasks. After simpler tasks, you will move on to the third module, Ansible Syntax and Playbook Development, where you will learn advanced configuration management implementations, and use Ansible Vault to secure top-secret information in your organization. In this module, you will also learn about popular DevOps tools and the support that Ansible provides for them (MYSQL, NGINX, APACHE and so on). The last module, Scaling Ansible for the enterprise, is where you will integrate Ansible with CI and CD solutions and provision Docker containers using Ansible.

By the end of the book you will have learned to use Ansible to leverage your DevOps tasks.

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
---
- include_vars: sensitive_data.yml
- name: Copy sensitive data file from Ansible control server to target hosts
  copy:
    content="{{secret_text}}"
    dest=/tmp/secret_text.txt
```



## Related Products
* [Implementing DevOps with Microsoft Azure](https://www.packtpub.com/networking-and-servers/implementing-devops-microsoft-azure?utm_source=github&utm_medium=repository&utm_campaign=9781787127029)

* [Ansible 2 for Beginners [Video]](https://www.packtpub.com/networking-and-servers/ansible-2-beginners-video?utm_source=github&utm_medium=repository&utm_campaign=9781786465719)

* [Implementing DevOps on AWS](https://www.packtpub.com/virtualization-and-cloud/implementing-devops-aws?utm_source=github&utm_medium=repository&utm_campaign=9781786460141)

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781787120532">https://packt.link/free-ebook/9781787120532 </a> </p>