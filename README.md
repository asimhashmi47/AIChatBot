<h1> AI Chat Bot </h1>

This repository contains a simple AI Chat Bot application using OpenAI's GPT-3.5-turbo model. The bot interacts with users through a command-line interface, providing responses generated by the AI model based on user prompts.

<h3> Table of Contents </h3>

<a href="#Installation">Installation</a>

<a href="#Usage">Usage</a>

<a href="#Code_Overview">Code Overview</a>

<a href="#Contributing">Contributing</a>

<a href="#License">License</a>

<h3 id="Installation"> Installation </h3>

1. Install the required packages:

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/6e82ac2f-9639-495e-a542-f328a377cb1a)

2. Set your OpenAI API key:

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/2a358fde-5d97-49c6-b3f4-200af67713da)

<h3 id="Usage"> Usage </h3>

Run the ChatBot.py script to start the chat application:

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/37dd3275-4d5f-4a6e-aa9f-a3a05516d61d)

<h3> Example Interaction </h3>

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/038a69b5-3392-4870-a698-7d77812c47c5)

<h3 id="Code_Overview"> Code Overview </h3>

Here is a brief explanation of the code:

<li> Imports and API Key Setup: </li><br />

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/33113e89-9fb9-4a07-9bbb-dd8b8dd374df)

<br />

<li> 'chatgpt' Function: </li><br />

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/6cd0491e-82a6-4a77-9e53-9522cf7b07b9)

<li> Takes a prompt as input. </li>
<li> Calls the OpenAI API to generate a response using the GPT-3.5-turbo model. </li>
<li> Returns the response text. </li>

<h3> Main Chat Loop: </h3><br />

![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/c9b0147f-3346-4b03-af4b-447dcc1b06ae)

<br /> 

<li> Runs an infinite loop to keep the chat interface active. </li>
<li> Prompts the user for input. </li>
<li> Checks for exit commands to end the chat. </li>
<li> Calls chatgpt to get a response from the AI and prints it. </li>

<h3 id="Contributing"> Contributing </h3>

We welcome contributions from the community! To contribute:

1. Fork the repository:

   <ul>
     <li> Click the "Fork" button at the top-right corner of the repository page on GitHub. </li>
   </ul>

2. Create a new branch:

   <ul>
     <li> Create and switch to a new branch for your feature or fix: </li> <br />

      ![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/0097f964-dd70-4ce8-a28a-331f026fe767)

   </ul>
   
3. Commit your changes:

   <ul>
     <li> Make your changes and commit them with a descriptive message: </li> <br />

      ![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/9321ca17-3950-4887-87a9-e6c443264d23)

   </ul>
   
4. Push to the branch:

   <ul>
     <li> Push your changes to your forked repository: </li> <br />

      ![image](https://github.com/asimhashmi47/AIChatBot/assets/38201527/2fdae55a-bc21-4482-8d51-42ec5a206681)

   </ul>
   
5. Fork the repository:

   <ul>
     <li> Go to the original repository on GitHub and click the "New Pull Request" button. </li>
     <li> Select your fork and the branch you created, then submit the pull request with a description of your changes. </li>
   </ul>

Please make sure your code adheres to coding standards and includes appropriate tests. This helps us review and integrate your contributions more efficiently.

<h3 id="License"> License </h3>
This project is licensed under the <a href="https://github.com/git/git-scm.com/blob/3ef6e50f1210ec893cfc9da7dc567edf04af5a06/MIT-LICENSE.txt">MIT</a> License. See the LICENSE file for details.

