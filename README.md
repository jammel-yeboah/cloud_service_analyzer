<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="http://www.cloudpricinganalyzer.com/">
    <img src="https://i.ibb.co/hmt2sLF/Cloud-Pricing-Analyzer.png" alt="Logo">
  </a>

  <h3 align="center">Cloud Pricing Analyzer</h3>

  <p align="center">
    Tell us what you want, and we'll give you the best cloud service to suit your needs!
    <br />
    <br />
    <br />
    <a href="http://www.cloudpricinganalyzer.com/">View Demo</a>
    ·
    <a href="http://www.cloudpricinganalyzer.com/more_info.html#contact-form-info">Report Bug</a>
    ·
    <a href="http://www.cloudpricinganalyzer.com/more_info.html#contact-form-info">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](http://www.cloudpricinganalyzer.com/)

A web application that allows users to find the best cloud service that suits their needs. Users will fill out a form, which will then be sent to multiple cloud services such as AWS, Azure, and GCP using their respective cloud billing APIs to get pricing info. The results are parsed and sorted based on several metrics such as pricing and computing capabilities. The most optimal cloud service for each provider is then displayed to the user. Users can also create accounts, save their reports and view past reports.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Flask][flask.com]][flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

There are a few you things you need to get installed before continuing

### Prerequisites

* pip
  ```sh
  python get-pip.py
  ```

### Installation


1. Get free authentication credentials:
   * [AWS Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-pelong.html)
   * [GCP Billing API](https://cloud.google.com/blog/topics/cost-management/introducing-cloud-billing-catalog-api-gcp-pricing-in-real-time)
   * [Recaptcha V2 Key](https://cloud.google.com/recaptcha-enterprise/docs/create-key)


2. Clone the repo
   ```sh
   git clone https://github.com/jammel-yeboah/cloud_service_analyzer.git
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file and enter your keys:
   ```js
   SECRET_KEY= ENTER AN ARBITRARY KEY
   AWS_ACCESS_KEY= ENTER YOUR API KEY
   AWS_SECRET_ACCESS_KEY= ENTER YOUR API KEY
   GCP_API_KEY= ENTER YOUR API KEY
   RECAPTCHA_PUBLIC_KEY= ENTER YOUR KEY
   RECAPTCHA_PRIVATE_KEY= ENTER YOUR KEY
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Start the flask server
   ```sh
   flask run
   ```

Search for a cloud service
1. On the landing page, click on "Get Started"
2. You'll be redirected to the "cloud form" page located in app/templates/cloud_form.html. Fill out the form based on your desired criteria
3. Upon clicking submit, you'll be displayed the results of your query


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jammel Yeboah - jammelyeboah@gmail.com

Project Link: [https://github.com/jammel-yeboah/cloud_service_analyzer](https://github.com/jammel-yeboah/cloud_service_analyzer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)
* [Font Awesome](https://fontawesome.com)
* [Heroku](https://www.heroku.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/jammel-yeboah/cloud_service_analyzer/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jammel-yeboah/
[product-screenshot]: https://i.ibb.co/FKJFShp/cpa-screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=flask&logoColor=white
[JQuery-url]: https://jquery.com
[flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/