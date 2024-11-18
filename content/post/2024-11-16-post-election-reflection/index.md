---
title: "Post-Election Reflection"
author: "Cathy Stanton"
date: "2024-11-16"
slug: "post-election-reflection"
categories: []
tags: []
---

<h2>
Recap of my 2024 Presidential Election Forecast Model
</h2>

This semester, I explored a variety of indicators and datasets week-to-week to predict the outcome of the 2024 U.S. Presidential Election. Most posts on this blog used one *type* of data (e.g. economic, polling, demographic, advertising) to predict the election outcome. For my final model, I chose to amalgamate data from across these sets into one big dataset, and then run a regression on each state, to see which predictors were most effective in explaining variance in Democratic Vote Share over time, based on their value for `\(R^2\)`. Then in each state, I fit a new multilinear regression just using the top 5 most predictive variables and predicted Democratic Vote Share based on that. For some variables, data comes from as far back as 1972. In creating a 2024 dataset to predict on, I had to use some *projected* metrics, which may have influenced my model’s accuracy (for example, I had to use projected demographic data since the last Census was conducted in 2020, and I had to use *projected turnout*, from the political scientist Michael McDonald’s prediction, because there did not exist *actual* turnout data for 2024 when I was making my prediction). My model did not make a prediction for Washington D.C. due to a lack of data, nor did it predict the national popular vote share, but it did generate percentages of the Democratic Vote Share in every state.

<h2>
Results and Accuracy of the Model
</h2>

The table below shows each state’s projected Democratic Vote Share (DVS) next to its actual, observed Democratic Vote Share in the 2024 Election. Cells with a DVS below 50% are shaded *red* because a Republican would have won them and cells with a DVS above 50% are shaded *blue.*

<div id="avifzfkhyo" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>#avifzfkhyo table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
&#10;#avifzfkhyo thead, #avifzfkhyo tbody, #avifzfkhyo tfoot, #avifzfkhyo tr, #avifzfkhyo td, #avifzfkhyo th {
  border-style: none;
}
&#10;#avifzfkhyo p {
  margin: 0;
  padding: 0;
}
&#10;#avifzfkhyo .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}
&#10;#avifzfkhyo .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}
&#10;#avifzfkhyo .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}
&#10;#avifzfkhyo .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}
&#10;#avifzfkhyo .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}
&#10;#avifzfkhyo .gt_column_spanner_outer:first-child {
  padding-left: 0;
}
&#10;#avifzfkhyo .gt_column_spanner_outer:last-child {
  padding-right: 0;
}
&#10;#avifzfkhyo .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}
&#10;#avifzfkhyo .gt_spanner_row {
  border-bottom-style: hidden;
}
&#10;#avifzfkhyo .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}
&#10;#avifzfkhyo .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}
&#10;#avifzfkhyo .gt_from_md > :first-child {
  margin-top: 0;
}
&#10;#avifzfkhyo .gt_from_md > :last-child {
  margin-bottom: 0;
}
&#10;#avifzfkhyo .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}
&#10;#avifzfkhyo .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#avifzfkhyo .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}
&#10;#avifzfkhyo .gt_row_group_first td {
  border-top-width: 2px;
}
&#10;#avifzfkhyo .gt_row_group_first th {
  border-top-width: 2px;
}
&#10;#avifzfkhyo .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#avifzfkhyo .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_first_summary_row.thick {
  border-top-width: 2px;
}
&#10;#avifzfkhyo .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#avifzfkhyo .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}
&#10;#avifzfkhyo .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#avifzfkhyo .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}
&#10;#avifzfkhyo .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#avifzfkhyo .gt_left {
  text-align: left;
}
&#10;#avifzfkhyo .gt_center {
  text-align: center;
}
&#10;#avifzfkhyo .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
&#10;#avifzfkhyo .gt_font_normal {
  font-weight: normal;
}
&#10;#avifzfkhyo .gt_font_bold {
  font-weight: bold;
}
&#10;#avifzfkhyo .gt_font_italic {
  font-style: italic;
}
&#10;#avifzfkhyo .gt_super {
  font-size: 65%;
}
&#10;#avifzfkhyo .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}
&#10;#avifzfkhyo .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}
&#10;#avifzfkhyo .gt_indent_1 {
  text-indent: 5px;
}
&#10;#avifzfkhyo .gt_indent_2 {
  text-indent: 10px;
}
&#10;#avifzfkhyo .gt_indent_3 {
  text-indent: 15px;
}
&#10;#avifzfkhyo .gt_indent_4 {
  text-indent: 20px;
}
&#10;#avifzfkhyo .gt_indent_5 {
  text-indent: 25px;
}
&#10;#avifzfkhyo .katex-display {
  display: inline-flex !important;
  margin-bottom: 0.75em !important;
}
&#10;#avifzfkhyo div.Reactable > div.rt-table > div.rt-thead > div.rt-tr.rt-tr-group-header > div.rt-th-group:after {
  height: 0px !important;
}
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
  <thead>
    <tr class="gt_col_headings">
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="state">state</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="predicted-D2PV">predicted D2PV</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="actual-D2PV">actual D2PV</th>
    </tr>
  </thead>
  <tbody class="gt_table_body">
    <tr><td headers="state" class="gt_row gt_left">Alabama</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">36.58</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">34.2</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Alaska</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">41.66</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">41.0</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Arizona</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">50.31</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">46.7</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Arkansas</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">27.86</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">33.5</td></tr>
    <tr><td headers="state" class="gt_row gt_left">California</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">55.86</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">58.8</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Colorado</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">28.95</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">54.2</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Connecticut</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">59.31</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">56.4</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Delaware</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">18.10</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">56.6</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Florida</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.21</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">43.0</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Georgia</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.53</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.5</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Hawaii</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">67.75</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">60.6</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Idaho</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">27.91</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">30.4</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Illinois</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">57.59</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">54.4</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Indiana</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">84.54</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">39.7</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Iowa</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">44.16</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">42.7</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Kansas</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">15.40</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">41.0</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Kentucky</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">38.07</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">33.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Louisiana</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">46.26</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">38.2</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Maine</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">27.68</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">52.1</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Maryland</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">100.45</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">62.4</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Massachusetts</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">67.12</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">61.3</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Michigan</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">47.18</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.3</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Minnesota</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">51.97</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">51.1</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Mississippi</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">44.20</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">37.3</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Missouri</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">40.43</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">40.1</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Montana</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">39.63</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">38.5</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Nebraska</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">40.71</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">22.5</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Nevada</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">45.90</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">47.5</td></tr>
    <tr><td headers="state" class="gt_row gt_left">New Hampshire</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">55.79</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">50.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">New Jersey</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">26.64</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">51.8</td></tr>
    <tr><td headers="state" class="gt_row gt_left">New Mexico</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">54.38</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">51.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">New York</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">49.24</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">55.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">North Carolina</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.76</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">47.8</td></tr>
    <tr><td headers="state" class="gt_row gt_left">North Dakota</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">31.96</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">30.8</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Ohio</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">40.32</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">43.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Oklahoma</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">34.69</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">31.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Oregon</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">56.08</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">55.6</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Pennsylvania</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">49.59</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.6</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Rhode Island</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">56.35</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">55.7</td></tr>
    <tr><td headers="state" class="gt_row gt_left">South Carolina</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">36.78</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">40.4</td></tr>
    <tr><td headers="state" class="gt_row gt_left">South Dakota</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">40.58</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">34.2</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Tennessee</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">37.45</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">34.5</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Texas</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">79.40</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">42.4</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Utah</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">19.88</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">37.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Vermont</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">64.37</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">64.3</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Virginia</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">80.33</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">51.8</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Washington</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">59.71</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">57.8</td></tr>
    <tr><td headers="state" class="gt_row gt_left">West Virginia</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">36.98</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">28.1</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Wisconsin</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #1874CD; color: #FFFFFF;">83.59</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">48.9</td></tr>
    <tr><td headers="state" class="gt_row gt_left">Wyoming</td>
<td headers="predicted D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">30.20</td>
<td headers="actual D2PV" class="gt_row gt_right" style="background-color: #B22222; color: #FFFFFF;">26.1</td></tr>
  </tbody>
  &#10;  
</table>
</div>
<h2>
Hypotheses of Inaccuracy
<h2>
<h3>
Number 1. Historical Trends
</h3>

The amount of data about each predictor varied: some predictors had data recorded since 1972, and others just to 2000. Additionally, some predictors (like polling averages) involved multiple data points per year, and others just provided a single point.  
The benefit of using data that stretches back to 1972 is that I had more results on which to train my model. That is, I had more data points about how the status of demographics, the economy, candidates’ polling, and advertising, impacted Democratic Vote Share. But since the political landscape looks vastly different today than in 1972 (with certain groups of voters swapping parties, and certain states reliably voting for a different party than they used to), the older data may bias the model.  
For predictors with multiple data points per year, I aggregated them into a mean and used that as the predictor value for the Democratic 2 Party Vote Share of that year. This could have impacted the model’s performance by neglecting to account for the (potential) association of *fluctuation* in values like polling averages in the months leading up to an election on Democratic Vote Share.

<h3>
Number 2. Equal Weight to All Variables
</h3>

To adjust for the inaccuracy of some historical data, I could have weighted the observations used to fit my state-by-state models based on how long ago they were taken relative to 2024. For example, I could have made observations from 1972 worth less than observations from 2020. To do this, I could have (1) linearly decreased the weights of data points based on how far away from 2024 they were (the drawback being that I might weight surprising/“once in a blue moon” outcomes more than typical outcomes if they were longer ago) OR (2) divided the data into `\(k\)` training and test sets, used the test set to measure the accuracy of the prediction made based on the data included in the training set, and then down-weighted the years (in the training set) whose models caused the highest test errors. The problem with this is that we cannot attribute innacuracy to specific years’ data because it might be due to the other data in its training set, or the sheer combination of years used in the training set. To account for this, we could select `\(k\)` in such a way that all permutations of years since 1972 can be the training set once, but it is still imperfect.

I also could have chosen to weight some *variables* more than others in the original multilinear regression. If I wanted polling data to appear in all of my states’ models, for example, and to be weighted more than the economic/demographic/advertising data in those states’ models, I could have multiplied it by a positive constant greater than 1, or multiplied the other features around it by some fraction before incorporating them into the regression.

<h3>
Number 3. Use of 5 Predictors in Every State
</h3>

Regardless of the `\(R^2\)` variables for the predictors in each state, I decided to use five predictors. In a future iteration of this model I could parameterize the number of predictor variables used in each state, either (1) selecting all of those features with an `\(R^2\)` value above some certain threshold (and only those features), (2) selecting predictors until the marginal returns on each state model’s accuracy is below some threshold, or (3) training models using different numbers of predictors (3, 4, 5, 6, etc.) and selecting those that have the best accuracy overall. To assess accuracy, I would keep some years in a training set and others in a test set and use out-of-sample error because, in predicting an election, we can’t use error based on the “truth” until the election occurs.

<h3>
Number 4. Collinearity
</h3>

We can see that some of the predictors, particularly demographic predictors, are highly correlated with each other. This is a common result when working with highly dimensional data. To reduce collinearity, I could apply regularization, either LASSO or Ridge. This is similar to the previous method of limiting the predictors in each state. But the previous method would not solely reduce dimensionality in all states… in some, it would probably increase dimensionality. To remove features associated with each other, LASSO and Ridge regularization penalize predictors by adding a penalty term to their sum of squared residuals, and then removing the features with the highest penalties plus squared residual sums. The penalty is based on a sum of the coefficients in the model. These regularization techniques reduce bias in the model by removing those terms with high sums of squared residuals, but the presence of the penalty term allows them to remove more features, the higher the dimension of the data.

<h3>
Number 5. Reliance on `\(R^2\)` Statistic
</h3>

`\(R^2\)` is the proportion of variance in the dependent variable explained by variance in the independent variable. But the interpretation of `\(R^2\)` changes when there are multiple predictors in a model. Similarly, the value of `\(R^2\)` for each respective predictor changes as the number of predictors in the model changes. Other statistics I could have used to select predictor variables to use in my models could have been the statistical significance (p-value) of their coefficient in the regression model, or I could have relied on a traditional regularization method (as described in the section above).

Overall, much of my model’s inaccuracy can be attributed to my goal of creating a *generalizeable* model to predict the 2024 Presidential Election outcome in each of the 50 states. Had I set out with a unique approach to predicting each state, potentially crafting 50 very different models, using different features, I may have wound up with different and/or better results.

<h2>
Tests to See if the Proposals Above Would Improve the Model
</h2>

The major issue with my model was high variance. Looking at the actual results, it’s true that Democratic Vote Share differs greatly between states (it was as low at 22.5% in Nebraska, overall, and as high as 64.3% in Vermont). But my model’s variance issues occurred in states like New York, Delaware, and Indiana where it severely over- or under-estimated Democratic Performance. On the contrary, when it was close to the actual Democratic 2 Party Vote Share in a state, it was very close. To test whether any of the above methods could solve this variance problem, I would generate an empirical distribution of past Democratic Vote Shares in each state (dating back to 1972, the start of my data) and see where each updated prediction falls within the distribution. The further away from the center of the distribution that an updated prediction falls, the less likely that the change in the method actually helped correct any error from the original model. However, if the correction moves the prediction closer within the bounds of previous Democratic Vote Shares in that state, I would adopt the correction into my model.

<h2>
What I Would Do Differently Next Time
</h2>

Next time I try to build a predictive model using features of different natures (e.g. economic data vs. demographic data vs. polling data) I would employ a Super Learning technique. This means building individual models for each state on each type of data, reserving some of that data for a test and then testing each state model’s accuracy on a prediction made with that test data, and then weighting the models’ outcomes in a linear supermodel based on how accurate each model was when tested on a test-set that is discrete from the data it was trained on. I also would not have shy-ed away from changing the methodology of each state’s model based on prior belief. This is a very Bayesian practice, but the way I would have done it in this model would have been very qualitative (based on the news, polls, and historical trends I was reading). In this year’s prediction, I wanted to avoid introducing my own bias into the model. However, in predicting something as volatile and nuanced as U.S. Presidential Election Outcomes, some bias might be favorable if it reduced the variance between predictions and reality. Something I learned this election cycle is that every pollster is different, and that they each introduce bias through the methods they choose to employ. For example, the famous historian Alan Lichtman chose to apply an entirely qualitative model, reflecting his own biases and experience from correctly predicting election outcomes from previous years. His method differed greatly from that of pollsters and quantitative social scientists, even if he could be just as confident in it.
