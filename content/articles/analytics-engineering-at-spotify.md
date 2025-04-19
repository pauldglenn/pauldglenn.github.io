Title: Analytics Engineering at Spotify
Date: 2020-12-03
Status: published
Category: Articles
Tags: analytics, engineering, spotify, data

# Analytics Engineering at Spotify

## Peter Gilks, Senior Director of Insights, Spotify Advertising

Since 2016 I've led the Insights team for Spotify's advertising business. Our role is to provide guidance that enables the product and business teams we work with to meet their objectives through evidence-based decision-making and customer focus. We're a multi-disciplinary team that covers both qualitative user research and data science, as per the Spotify model. Our work includes exploratory analysis, experimentation, metric setting, building dashboards, user testing, ethnography, and surveys.

The data scientists on the team spend a good chunk of time on that old favorite that never seems to go away — data preparation. At Spotify, we have a continuously evolving and growing volume of data at our fingertips. As we launch new features and develop new products, we instrument our product to capture the right data, transform it into something usable for analysis or experimentation, and build pipelines to keep it coming. And as we expand and transform our business, we are always looking at how we cut and slice that data to make sure we're keeping up with the questions we are trying to answer. In short, we need to make our data 'analytics friendly' (thank you to Rishi Nalin Kumar from whom I picked up this term).

A few years ago, I recognized that this stage of data preparation, to make it 'analytics friendly', was becoming a challenge for my team of data scientists. They could do it, but they were doing it independently. Applying business logic, choosing levels of aggregation, grouping and transforming fields, checking data quality and cleaning data — these are all crucially important tasks, but they are also enormously time-consuming not to mention prone to error and inconsistency if they are done anew for each piece of analysis.

It struck me as I reviewed work that the SQL gymnastics my team members were each performing were at once both impressively masterful, but also disappointingly inefficient. So we set off to look for solutions — starting with considering what key datasets we could build that would be used by the whole team to save time and improve consistency. My goal as expressed to the team was "take a bunch of SQL this big and make it this small" [insert picture of me stretching my hands as vertically far apart as possible, followed by a short gap between my thumb and forefinger].

> "As we expand and transform our business, we are always looking at how we cut and slice that data to make sure we're keeping up with the questions we are trying to answer."

We tried a couple of approaches to achieve this. One was to ask our friends in data engineering to help, but it was hard to make this work a smart priority for them for two reasons. One is that they have plenty of production work to do on our live systems, the other is that the understanding that is required to express how to make data 'analytics friendly' and helpful for a group of data scientists takes a lot of translation time, and back and forth.

The other effort was to do this work collectively 'on the side of our desks'. But despite a keen start this effort also fell by the wayside as other priorities came along and questions of ownership became difficult to untangle.

This is the point at which I thought "what we really need is someone who does this as a full time job". I wanted to find someone who had the experience of working in analytics and data science and understood the joys and the pains of that job, who was passionate about data quality, documentation and SQL efficiency, who was better at data engineering than most data scientists but who didn't want to be a data engineer and who could coach others in these skills. Not much to ask for right?

So in early 2018 we put out a job ad for something called an 'analytics data specialist'. The tagline of the job description read "We are looking for an expert in building out analytical data layers to join the band and help drive a data-first culture across the ad-supported business in Spotify". Catchy.

Somehow we found Paul and he quickly got to work revolutionizing our approach to data. The impact has been enormous. We are more effective and efficient than ever before. The time it takes us to turn around analysis is vastly reduced, the confidence and consistency in our results is increased and because the 'barrier to entry' for data is reduced we can share and collaborate across teams seamlessly. We have since invested further, building out our own team and spreading the gospel throughout the company.

When we hired Paul he was quick to let me know that 'analytics data specialist' is a terrible job title. So we went with 'analytics engineer' instead...

> "The time it takes us to turn around analysis is vastly reduced, the confidence and consistency in our results is increased and because the 'barrier to entry' for data is reduced we can share and collaborate across teams seamlessly."

## Paul Glenn, Senior Analytics Engineer, Spotify Advertising

At Spotify, we've spent the last two years initiating, defining and evolving the role of analytics engineer. Peter was not alone in his realizations about the key problems data practitioners at Spotify faced, and when Michael Kaminsky's blog post on analytics engineering dropped just a few weeks after we'd settled on the same job title for my role, it was a very clear signal that we were on the right track.

Early on, I described the role of an analytics engineer as someone who "reduces the complexity surface data scientists need to engage with in order to create meaningful insights." We try to achieve that in several ways:

**1. Create, maintain, support, and evolve a clean data ecosystem**

Spotify's business is large, complex and constantly evolving, and our data is even larger, more complex and more rapidly changing. A model where data scientists are staffed to projects, learn about and clean the necessary data, gather and standardize business requirements, produce an analysis, and move on, is not sustainable. Our first analytics engineering project was to review the landscape of projects and business needs, then consolidate the data into a handful of tables that would cover 80% of the data scientists' needs.

Such an effort had been undertaken several times before, but the difference this time was the presence of dedicated support. My team's contract with our users is to make sure the data keeps flowing free of bugs, to quickly provide answers to questions about the data's provenance, reliability and applicability, and to add new columns — or gracefully deprecate and replace datasets — as the business changes.

**2. Provide engineering support to data practitioners, evangelize existing tools, and build new tools**

It was once said that data scientists are data engineers who can do statistics. But with the evolution and growth of the role, and the complexity of our internal infrastructure, it's not reasonable to expect a data scientist to know how to do every engineering task or understand every underlying system involved in their day-to-day role. In addition to supporting our datasets, analytics engineers at Spotify use their dual knowledge of the most important tools and infrastructure, and the day-to-day experience of the data scientists we closely work with to provide support for common engineering challenges. We help make sure that nobody is "reinventing the wheel" and provide training and on-boarding for new hires. When there are gaps in the overall workflow, we're in a good position to recognize them and see potential solutions, leading to several new internal tools developed by analytics engineers.

**3. Use our central position and knowledge of available data to coordinate and assist on cross-team projects**

Many analytics engineers at Spotify were data scientists at one point in their careers, and most still like to throw on their insights hat and dive into the data from time to time. Because we get to touch a lot of different datasets and work with data scientists from many different teams in our day-to-day work, we're well positioned to coordinate cross-team efforts and provide data support to very large projects. In addition to being sometimes our most visible impact, this sort of work allows us to engage with the challenges data scientists face every day and "eat our own dog food" to better understand and hone the datasets and tools we build and maintain.

While it may sound like we have analytics engineering all figured out at Spotify, one of the most exciting parts of the job is that we are in fact constantly evolving definition of the role — something that seems to be happening all over the industry. With every new blog post that comes out, whether from Michael Kaminsky, DBT, Netflix or the many others who have written on this topic, we see both echos of the journey we've already taken and ideas for new opportunities we can take on.

The flexibility to make the role of analytics engineer whatever it needs to be is certainly my favorite part of the job. I sometimes say that my career archetypes are editor and librarian. As an analytics engineer, I get to play both of those roles frequently. Like an editor works with a writer to hone and improve their writing, I think of a key part of my role as working with data scientists and other stakeholders to hone and improve their processes for gathering, understanding, and interpreting data. And like a librarian works with a researcher to identify and retrieve resources, we analytics engineers can use our understanding of the data landscape to direct our stakeholders to the right resources to answer the pressing business questions they're faced with.

*If you'd like to explore career opportunities in analytics engineering at Spotify, please check for postings on our [job page](https://www.spotifyjobs.com/).*

# Credits

**Peter Gilks**  
Senior Director of Product Insights  
—  
**Paul Glenn**  
Senior Analytics Engineer 