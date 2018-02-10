# WhoRepresentsYou
Senior Project for Ramapo College

http://www.WhoRepresentsYou.com

This project is planned to be a combination of two tools.

First, there will be an email notification system.

When a representative votes on a bill with a user specified keyword, you can get an email notification.

Second users can see the positions representatives have based on their voting history in their seat.
A user would indicate what issues they are interested in hearing about.

From their past votes on any legislation with the keywords specified.
TextBlob library will be used to interpret the legislation's synopsis' sentiment, and more specifically the polarization.

With this info, along with how they voted, I can determine to a rough degree, where the representative stands on that issue(keyword).

The planned algorithm to process the voting data is a work in progress.
It is very possible this will cause data to float very close to the midpoint, or for some other anomaly to occur.

The Scaling Process (WIP)
  The user specifies a keyword or group of keywords for a representative.
  Next we pull the list of votes that could have occurred.
  We use the most recent 1/3 of their total time as a representative to get bills or up to 30 in total, whichever is greater.
    There may not be many votes and we should keep that in mind.
  From this one third, we group them together into a list of bill lists.
  We group all the votes on one bill, with amendments, so that multiple votes on one bill does not overpower the data.
    We process the data on a bill by bill basis, the first vote is weaker than the last vote, as passing a bill is more important than letting it move to another step.
  Sentiment Analysis from Python TextBlob Library will allow me to extract positive or negative connotations - data[X][Y].sentiment , a real from [-1, 1]
  The other piece of data is their vote
    A Yes is a 1
    A No is a -1
    An Abstain is a 0
    An excused Absence would also constitute a 0, but further absence would also degrade the accuracy of the signaling.
      This is recorded outside of the independent vote in a counter for all absentee votes.
      This counter would be divided by (the number of votes in total times 2) to produce the +/- range of the overall indicator.
        Ex: There are 60 votes, and 12 are absentee votes, then we do 12/120 = 1/10 = 0.1.
          So the overall indicator would be the average of the data as normal, say +0.38, but with this range making it from 0.28 to 0.48, which makes it quite inaccurate.
          Abstains and absentees are rare and therefore should not completely destroy the data, but have an impact on the analysis when present.
