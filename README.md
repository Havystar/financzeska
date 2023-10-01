# Chat Data Explorer

Project description
Our project aims to create a powerful and user-friendly chatbot that facilitates the retrieval of information from various data sources and assists users in analyzing the acquired data by always providing a source. Similar to the Bing chatbot, our solution is designed to be efficient and intuitive. Below, we provide a detailed overview of our project's technical architecture, technologies, and key features. In the future, we would like to add some cool charts or simplified tables to highlight the exact data you need.


Technologies and Solution Architecture:

Backend:

FastAPI: We have chosen FastAPI as our microservice framework for its speed, simplicity, and compatibility with modern Python libraries, making it an excellent choice for developing robust backend services.
LLama.cpp: Our self-hosted LLM runner, LLama.cpp, plays a pivotal role in understanding and processing natural language queries effectively.
Nginx: As a reverse proxy, Nginx ensures efficient routing of incoming requests and enhances the overall performance and security of our system.
ROCm: While our solution is fully compatible with CUDA, we are currently leveraging ROCm as our primary compute platform. This choice allows us to make the most of available hardware resources.
Frontend:

React: We use React as our JavaScript framework to build a dynamic and responsive user interface, ensuring a smooth and interactive user experience.
MUI (Material-UI): MUI is our chosen UI framework, providing a consistent and visually appealing design for the frontend components.


Architecture:

Our chatbot architecture consists of two primary microservices that interact with the React frontend seamlessly:

Dataset Selection Microservice: This microservice assists users in choosing the correct dataset from a wide range of available sources.
Data Analysis Microservice: The data analysis microservice supports users in analyzing the selected data, making it easy to extract valuable insights.
We place a strong emphasis on ensuring a cohesive and user-friendly interaction between these microservices and the React frontend, prioritizing a seamless user experience.



Data Sources:

Our initial focus is on enabling access to over 100 different data sources from dane.gov.pl. However, our system's flexibility allows us to adapt and incorporate additional data sources as needed to meet evolving user requirements.



Potential Monthly Costs:

As of now, our solution does not rely on external APIs beyond data sources, resulting in minimal monthly expenses. Assuming that computational resources are provided by the host, the primary cost would be electricity. We are currently running our program on consumer-grade AMD hardware, which may not be optimal, but it minimizes the financial burden.



In conclusion, our chatbot project aims to provide users with a powerful and intuitive tool for accessing and analyzing diverse datasets. With a well-thought-out architecture and a focus on cost efficiency, we are poised to create a valuable resource for information retrieval and analysis.
