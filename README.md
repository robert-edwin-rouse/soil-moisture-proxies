# soil-moisture-proxies

<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT HEADER -->
<br />
<div align="center">
  <a href="https://github.com/robert-edwin-rouse/soil-moisture-proxies">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Streamflow Prediction Using Artificial Neural Networks &amp; Soil Moisture Proxies
</h3>

  <p align="center">
    <br />
    <a href="https://github.com/robert-edwin-rouse/soil-moisture-proxies/issues">Report Bug</a>
    ·
    <a href="https://github.com/robert-edwin-rouse/soil-moisture-proxies/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](./figures/54057-P-2012.png)

This codebase accompanies the Environmental Data Science paper 'Streamflow Prediction Using Artificial Neural Networks &amp; Soil Moisture Proxies'.  It includes the code to download the requisite ERA5 data from the ECMWF Copernicus Data Store, the code to run the model and reproduce all of the results, and reproduce the main figures from the paper.

In order to maximise flexibility, core functions are shared between this project and related projects through the apollo environmental data science submodule; the version required to reproduce the results in the paper is included but may not be the most up to date version.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The catchment database file included in this repository has been left underpopulated, as the data to fully populate it is owned by the Centre for Ecology and Hydrology; this is open source data that can be accessed through the National River Flow Archive https://nrfa.ceh.ac.uk/data/search.  Downloading the data from the ECMWF CDS requires the creation of an API key, instructions for which can be found on the following page https://cds.climate.copernicus.eu/api-how-to.

### Prerequisites

The apollo submodule, which contains an evolving range of environmental data science functions and some of which are used within this project, can be found at https://github.com/robert-edwin-rouse/apollo.  Both apollo and this repository rely on standard python libraries, including:
  * numpy
  * math
  * pandas
  * datetime
  * matplotlib

The following additional libraries/packages are also required:
  * cdsapi
  * xarray
  * geopandas
  * pytorch
  * scikit-learn

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

1. This repository can be installed from the command line via:
   ```sh
   git clone https://github.com/robert-edwin-rouse/soil-moisture-proxies.git
   ```
2. The most up to date version of apollo can be installed via:
   ```sh
   git clone https://github.com/robert-edwin-rouse/apollo.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Provided the catchment database csv file has been populated with data for the target catchments, the 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Simplify the model script
- [ ] Add code to reproduce violin plots

See the [open issues](https://github.com/robert-edwin-rouse/soil-moisture-proxies/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/robert-edwin-rouse/soil-moisture-proxies](https://github.com/robert-edwin-rouse/soil-moisture-proxies)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/robert-edwin-rouse/soil-moisture-proxies.svg?style=for-the-badge
[contributors-url]: https://github.com/robert-edwin-rouse/soil-moisture-proxies/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/robert-edwin-rouse/soil-moisture-proxies.svg?style=for-the-badge
[forks-url]: https://github.com/robert-edwin-rouse/soil-moisture-proxies/network/members
[stars-shield]: https://img.shields.io/github/stars/robert-edwin-rouse/soil-moisture-proxies.svg?style=for-the-badge
[stars-url]: https://github.com/robert-edwin-rouse/soil-moisture-proxies/stargazers
[issues-shield]: https://img.shields.io/github/issues/robert-edwin-rouse/soil-moisture-proxies.svg?style=for-the-badge
[issues-url]: https://github.com/robert-edwin-rouse/soil-moisture-proxies/issues
[license-shield]: https://img.shields.io/github/license/robert-edwin-rouse/soil-moisture-proxies.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[product-screenshot]: ./figures/54057-P-2012.png