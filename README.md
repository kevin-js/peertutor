<h1>PeerTutor</h1>
<h3>Best Practices</h3>

<h6>Developing locally</h6>
<p>When developing on your local machine, it is good to use virtualenv to create a virtual Python environment and install all needed Python packages from the requirements.txt file. This will ensure that everyone is on the same page with regards to dependencies and that you don't accidentally modify your global Python environment on your computer. A quick tutorial to virtualenv can be found at https://virtualenv.readthedocs.org/en/latest/</p>
<p>Before making any changes, make sure your local git repository is up-to-date with the remote GitHub repo; this will circumvent the need to resolve gnarly merge conflicts down the road.</p>

<h6>GitHub repository structure</h6>
<p>There will be several workstreams on this repository. The description for each branch is as follows:</p>
<ul>
	<li>master: This branch will be the most up-to-date stable site used for the production build. Changes will be pushed to this branch only after passing code review and testing.</li>
	<li>staging: This branch is the working branch tracking development progress. Individual commits will be merged after passing a code review.</li>
	<li>staging/&lt;username&gt;: When pushing individual commits from your local machine to the GitHub repo, follow this naming format for naming your branch. An admin will perform a code review and if everything looks good, the commit will be merged into the main staging branch.</li>
	<li>If you want to experiment with additional features or make significant changes, create a new branch with your additions. This will help make it easier to manage different versions of the site.</li>
</ul>

<h6>To commit changes:</h6>
<ol>
	<li>Commit your changes to a new branch in your Git repo and push upstream.</li>
	<li>Open a pull request on GitHub; myself or another an admin will review the changes and merge into the master branch if all is well.</li>
	<li>If it is a particularly urgent update, shoot me a blitz or text me and I'll try to take a look at it ASAP.</li>
</ol>