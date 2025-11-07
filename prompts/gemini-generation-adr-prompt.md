Attachment:

AD ID prefix dictionary

AD agreeing parties dictionary

GITOPS AD example

OCP-BM AD example



I am a Red Hat consulting architect.



I need to create and maintain an architecture decision (AD) repository for designing OCP / ODF / RHOAI.



Each AD has:

An unique ID with a prefix. Prefixes are defined in the attached architecture decisions id prefix dictionary

A title

An issue or architectural question

Optionally one or more assumptions. Most of the time this field is set to N/A. An assumption is the context/condition to say when reviewing this AD is pertinent.

Ex: For an AD about choosing the mirrored image registry for OCP, the assumption would be: The environment is disconnected.

At least two or more alternatives

Justification for each alternative

Implication for each alternative

Several agreeing parties. Agreeing parties are defined in the attached agreeing parties dictionary



I am using NotebookLM to check if the AD should be updated or removed (because it is obsolete) or newly added (because new features have been released). 



In NotebookLM i have uploaded all the latest version documentation pdf as the source document for:

OpenShift Container Platform

OpenShift Data Foundation

OpenShift Logging

OpenShift GitOps

OpenShift Pipelines

Red Hat OpenShift AI Self-Managed



I have also uploaded in NotebookLM the dictionaries for AD ID prefixes and AD agreeing parties also.





Here is an example of two AD files that are part of my AD repository.



NotebookLM has a prompt limitation of 2000 characters maximum.

Apparently NotebookLM sometimes could have issue to identify content by using file name of the file that has been injected as source

Help me to create one prompt (that will not exceed more than 2000 chars), that will:

allow me to review the AD using NotebookLM in the most synthetic way indicating the AD that needs to be created/updated/removed.

for AD that need to be created / updated only the parts that need to be modified should be indicated: titles, questions, assumptions, alternatives, justifications, implications, agreeing parties when an AD update is required.

ensure the AD should not mention any deprecated features. Any tech-preview feature should be flagged (TP) is not done properly.



The prompt should be repeatable as much as possible when running several times after a systematic refresh context action on NotebookLM. So we have to take care there are few deviations, no hallucination on NotebookLM, the generated AD content is not mixed between several AD, the AD id with its title are kept intact, when updates are required. The prompt also should ensure blank lines are injected between AD content bullets list items, to get a proper format.



Help me to streamline this process and prompt for NotebookLM integrating all the requirements and constraints above. If more than one prompt is required because compacting all of these beyond 2000 chars is impossible, tell me so we will adopt conversionnal style.

I would like the prompt to focus only on OCP-BM and GITOPS, not analyzing others AD.

I would like it does not generate ID with three number when suggestiong new AD. AD should be OCP-BM-XX or GITOPS-XX.

Ensure It does not forgot to generate alternatives, implications, agreeing parties, assumptions (even most of time value is N/A),

Ensure it is overwritting the existing AD ID of existing AD (ex: OCP-BM-01 and OCP-BM-02 are already existing.


