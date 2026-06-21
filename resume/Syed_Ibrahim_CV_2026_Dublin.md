# Syed Ibrahim

**Senior Full-Stack Developer (Java / React)**

Lucan, Co. Dublin · 089 973 3809 · Ibrahim.syed.r@gmail.com

---

## Professional Summary

Senior full-stack engineer with **20+ years** of Java experience, based in Dublin and working across financial services and enterprise platforms. Specialist in **Spring Boot microservices**, REST APIs, cloud-native delivery on **AWS (EKS)**, and production support at scale; **React micro-frontends (MFE)** for customer-facing booking flows.

Strong track record designing and delivering secure, high-throughput services for **Hertz**, **Mastercard**, **AIB**, and other regulated environments. Comfortable across the full delivery lifecycle — architecture, implementation, CI/CD, Kubernetes deployment, observability (Splunk, Dynatrace, Amplitude), and production incident resolution. Built and deployed a **React.js timesheet application** as a personal full-stack side project, integrated with Spring Boot microservices on AWS.

---

## Core Skills

| Area               | Technologies                                                                                                       |
| ------------------ |--------------------------------------------------------------------------------------------------------------------|
| **Backend**        | Java 17, Spring Boot, Spring Security, Spring Batch, Spring Retry, REST, OAuth2 / JWT, JPA / Hibernate             |
| **Integration**    | Kafka, IBM MQ, SOAP / REST, message-level encryption, two-way SSL                                                  |
| **Cloud & DevOps** | AWS (EKS, Lambda, API Gateway, CDK), Kubernetes, PCF, Docker, GitLab CI                                            |
| **Observability**  | Splunk, Dynatrace, Amplitude, SonarQube, Seemplicity                                                               |
| **Data**           | Oracle, SQL, JPA; XML / XSD / JAXB                                                                                 |
| **Frontend**       | ReactJS, TypeScript, Module Federation (MFE), React Router, Tailwind CSS, Angular, AngularJS, JavaScript, HTML/CSS |
| **Practices**      | Agile / Scrum, TDD, BDD (Cucumber, JBehave)                                                                        |

---

## Professional Experience

### Hertz — Dublin

**Senior Full-Stack Developer** · Mar 2021 – Present

- Maintain and enhance **Spring Boot microservices** supporting mobile and web applications; primary backend contact for mobile API integration.
- Re-factored the **authentication service** used by frontend and mobile clients, implementing **Spring Security** for REST API access.
- Worked in **React MFE** features for international shop-and-book app
- Built **Splunk** and **Dynatrace** dashboards for production monitoring; debugged and resolved production and lower-environment incidents.
- Contributed to **AWS CDK** (TypeScript / Python) projects exposing Lambda functions via private API Gateway and VPC endpoints.
- Optimised **IBM MQ** connection handling and service performance under production load.
- Built **htzd-shop-and-book-mcp**, a **Spring AI** MCP server exposing Hertz rental APIs as AI tools (vehicle search, location lookup, reservation create/lookup/cancel) for chatbot and assistant integration deployed on **AWS EKS**.
- Implemented a secure REST API proxy and OpenAPI integration for Hertz car rental booking via ChatGPT — OAuth 2.0, multi-endpoint orchestration.

---

### Mastercard — Dublin

**Lead Java Developer** · Feb 2018 – Mar 2021

- Designed and delivered the **ABU Push** suite of microservices on **Spring Boot**.
- Built a proof of concept for **message-level encryption** (asymmetric and symmetric keys) in a customer-facing application.
- Improved throughput via **multi-threading**, connection pooling (MQ, HTTP), and **circuit breaker** patterns.
- Developed and troubleshooted **Kafka** producers and consumers; deployed and debugged services on **Pivotal Cloud Foundry**.
- Established **Splunk** dashboards, alerts, and query-based diagnostics; enforced quality gates with SonarQube and Checkmarx.

**Stack:** Spring Boot, Spring Batch, Spring Retry, EhCache, PCF, Kafka, Splunk

---

### Aristotle IT Services — Dublin _(consultant placements)_

**Java Consultant** · May 2013 – Jan 2018

#### Allied Irish Bank · Feb 2017 – Jan 2018

- Designed and built **JSON REST services** on Spring Boot.
- Implemented **JWT authorisation** with Spring OAuth2 and JJWT for multiple consumer applications.
- Delivered **two-way SSL** with common-name validation; unit and integration tests with Spring Test, JUnit, Hamcrest.

#### Bearing Point · Jun 2016 – Feb 2017

- Full-stack delivery for passport renewal workflows: AngularJS UI, **Activiti BPMN**, JPA entities, XSD design for printing-system messages.
- Input validation, PDF reporting, and workflow task executors.

#### 123.ie · Feb 2016 – May 2016

- Responsive UI development with AngularJS and CSS3 media queries across mobile and desktop.

#### Bank of America · Aug 2015 – Feb 2016

- REST APIs for the Diamond UI application (**Python / Flask / SQLAlchemy**, Knockout.js).

#### Bearing Point · Jun 2014 – Jun 2015

- Spring REST controllers, **Spring Security**, JPA, SOAP/REST integration; Agile/Scrum delivery.

#### Bord Gáis · May 2013 – May 2014

- Standalone Java application generating **PAIN.008** payment XML; JAXB, JPA/Hibernate, JSR-303 validation.
- XSLT transforms for PAIN.002 failure analysis and Excel-based reporting.

---

### Barclays Technology Center — Singapore

**Java Consultant** · Apr 2012 – Apr 2013

- Backend development for **iBOC**, an intermediary between core banking services and an iOS iPad app for remote account opening (Spring MVC, JPA, JSON, web services).

---

### HeiTech Padu Berhad — Malaysia

**Java Consultant** · Nov 2011 – Apr 2012

- JPJ (Road Transport Department) project: ZK UI, JPA, EJB, IBM RAD web services.

---

### HP — India

**Java Consultant** · Aug 2010 – Nov 2011

- Legacy modernisation for **General Motors**: Struts/JSP UI, Spring-WS web services exposing mainframe data.
- Greenfield **Centralised Rate Repository (CRR)**: JSF 2.0 Facelets, JPA, Oracle.

---

### Cognizant Technology Solutions — India

**Senior Associate** · Dec 2009 – Jul 2010

- Migrated VB standalone app to Java Swing for **AstraZeneca**; designed core search functionality (JDOM).
- Re-platformed portal from WebSphere to Tomcat for **Schering-Plough** (Struts, Spring, Hibernate).

---

### Verizon Data Services — India

**Java Developer** · Jan 2008 – Dec 2009

- **Enterprise Product Catalog (EPC)**: EJB session facade, Spring wiring, JDOM XML, Oracle SQL\*Loader data feeds, XSL-to-HTML transforms.

---

### Polaris Software Lab — India

**Java Developer** · Sep 2005 – Dec 2007

- Client delivery for **Hitachi, Japan**: Electronic Approval System (JSP/Servlets), Struts/Hibernate localisation (NAS GUI), XML/XSLT expertise (Xalan/Xerces testing), design documentation.

---

## Personal Projects

### SLR Timesheet App — Side Project · [slrtime.click](https://slrtime.click)

**Full-stack developer** · Feb 2025 – Present

End-to-end timesheet management application: React SPA with Spring Boot authentication and data services, deployed on **AWS EC2** behind **Nginx** with HTTPS.

- Built the **React JS** frontend (Create React App) with **React Router**, **Material UI**, **Tailwind CSS**, and **React Hook Form** for timesheet entry, project tracking, notes, and admin workflows.
- Implemented **JWT authentication** with refresh-token handling, protected routes, role-based admin access, OAuth2 support, and RSA password encryption via the Web Crypto API.
- Integrated with **Spring Boot REST APIs** for auth and timesheet data; designed fetch-based HTTP client with automatic token refresh and CSRF handling.
- Deployed production build as static assets on **AWS EC2** with **Nginx** reverse proxy, Let's Encrypt SSL, and SPA routing fallback.

**Stack:** React JS, MUI, Tailwind CSS, React Router, Context API, Spring Boot, JWT, Nginx, AWS EC2

---

## Education

**Master of Computer Applications (MCA)** — 76.8%

---

## Certifications

- Cloudera Certified Apache Hadoop Developer (CCDH-410) — 81%
- Sun Certified Java Programmer (SCJP 1.4) — 88%
- Sun Certified Web Component Developer (SCWCD 1.3) — 84%
- Sun Certified Business Component Developer (SCBCD 2.0) — 92%

---

## Additional Information

- **Location:** Lucan, Co. Dublin
- **Languages:** English (professional)
- **Work authorisation:** Based in Ireland; eligible to work in Dublin without relocation
