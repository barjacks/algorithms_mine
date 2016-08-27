# Before anything else, start installing OpenCV!

**OS X:**

First install OpenCV using `brew`

    brew tap homebrew/science
    brew install opencv3 --with-contrib --with-python3 --with-ffmpeg --with-tbb --with-qt5
    
and then in like an *hour* you'll be able to run the next line.

    echo /usr/local/opt/opencv3/lib/python3.5/site-packages >> /usr/local/lib/python3.5/site-packages/opencv3.pth

**Windows:**

Follow [these instructions](https://scivision.co/install-opencv-3-0-x-for-python-on-windows/) to install the `whl` file (I'm pretty sure you've done similar things before) - if that doesn't work, install the [pre-built binaries for Python 2](https://breakthrough.github.io/Installing-OpenCV/).

# Before anything else, also sign up for Google BigQuery!

[Google BigQuery](https://cloud.google.com/bigquery/) is a big... querying engine, with lots of data. Make sure you can log in and create projects.

You'll eventually end up at [bigquery.cloud.google.com](bigquery.cloud.google.com).

    SELECT *, 
    DATE_PART('HOUR', TO_TIMESTAMP(dropoff_datetime)) * 60 + DATE_PART('MINUTE', TO_TIMESTAMP(dropoff_datetime)) AS the_time
    FROM results_20160825_105234

# Some links for today

* [OpenCV](http://opencv.org/)
* [Google BigQuery](https://cloud.google.com/bigquery/)
* [The Interactive Way to Go](http://playgo.to/iwtg/en/)
* [COSUMI](http://www.cosumi.net/en/), browser-based go