from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse(
<!DOCTYPE html>
<html>
<head>

<!-- FHH COMMENTED OUT
<script	src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
-->

<script>
/*
* show and hide descriptions for services
*/
showHideDesc = function(id, ctx){
var approvedNum = id;
var descNum = "desc"+id;
var dropText = "more"+id;
var origin = window.location.protocol + "//" + window.location.host + ctx;
if(document.getElementById(approvedNum).alt == "image of plus symbol"){
	document.getElementById(approvedNum).src = "https://gateway.usps.com/eAdmin/images/gui/bkg/icons/minus-grey.png";
	document.getElementById(approvedNum).alt = "image of minus symbol";
	document.getElementById(descNum).style.display = "block";
	document.getElementById(dropText).alt = "less"+id;
	document.getElementById(dropText).title = "Click to minimize";
	document.getElementById(dropText).innerHTML = "less info >";
}else{
	document.getElementById(approvedNum).src = "https://gateway.usps.com/eAdmin/images/gui/bkg/icons/plus-grey.png";
	document.getElementById(approvedNum).alt = "image of plus symbol";
	document.getElementById(descNum).style.display = "none";
	document.getElementById(dropText).alt = "more"+id;
	document.getElementById(dropText).title = "Click to learn more"
	document.getElementById(dropText).innerHTML = "more info >";
}
};	
</script>

 
<title>USPS Business Customer Gateway</title>
<meta name="keywords" content="" />
<meta name="description" content="" />

<link rel="shortcut icon"
	href="https://gateway.usps.com/eAdmin/images/favicon.ico"
	type="image/x-icon">

<link rel="stylesheet"
	href="https://gateway.usps.com/eAdmin/scripts/dojo/themes/claro/claro.css">
<link rel="stylesheet"
	href="https://gateway.usps.com/eAdmin/styles/gui/common-usps.css"
	type="text/css" media="all" />
<link rel="stylesheet"
	href="https://gateway.usps.com/eAdmin/styles/gui/bcg.css"
	type="text/css" media="all" />

<link rel="stylesheet"
	href="https://gateway.usps.com/eAdmin/styles/gui/displaytag.css"
	type="text/css" media="all" />

<link rel="stylesheet" type="text/css"
	href="https://gateway.usps.com/eAdmin/styles/gui/custom.css" />

<link rel="stylesheet" href="https://gateway.usps.com/eAdmin/styles/gui/modalbox.css" type="text/css" media="all" />
<link type="text/css" href="https://gateway.usps.com/eAdmin/styles/gui/themes/flick/jquery-ui-1.8.24.custom.css"
	rel="Stylesheet" />
<link type="text/css" href="https://gateway.usps.com/eAdmin/styles/gui/datepicker.css" rel="Stylesheet" />
<link type="text/css" href="https://gateway.usps.com/eAdmin/styles/bootstrap-iso.css" rel="Stylesheet" />
<link type="text/css" href="https://gateway.usps.com/eAdmin/styles/gui/redesign.css"	rel="Stylesheet" />
	<link media="all" type="text/css"
	href="https://gateway.usps.com/eAdmin/styles/gui/progress-bar.css"
	rel="stylesheet">
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">


<!-- FHH COMMENTED OUT     
<script>
	dojoConfig = {
		has : {
			"dojo-firebug" : false
		},
		parseOnLoad : true,
		foo : "bar",
		async : true
	};
</script>
<script type="text/javascript"	src="https://gateway.usps.com:443https://gateway.usps.com/eAdmin/scripts/dojo/dojo.js"></script>

<script type="text/javascript" src="https://gateway.usps.com:443https://gateway.usps.com/eAdmin/JavaScriptServlet"></script>
--> 

</head>

<body class="claro" id="pageBodyId">
	<!-- begin #page -->
	<div id="page">	
		<div class="bootstrap-iso pt-0 mt-0 mb-0 pb-0">
			<nav id="myNavbar" class="navbar " role="navigation">
				<!-- Brand and toggle get grouped for better mobile display -->
				<div class="container-fluid navbar-gradient pt-0 mt-0 mb-0 pb-0">
					<div class="container">
						<div class="row">
							<div class="col-12">
								<div class="nav navbar-header" id="navbarAfterLogin">
									<div class="row navbar-nav mb-0 pb-0" style="padding-top: 1%;">
										<img
											src="https://gateway.usps.com/eAdmin/images/gui/usps-logo-withouttext.png"
											class="img-fluid " height="20px" title="USPS logo"
											alt="USPS logo image of blue eagle" /> <a
											href="https://gateway.usps.com/eAdmin/action/homepage">
											<img							
											src="USPS-BusinessPartnerGateway.png"
											class="img-fluid" tabindex="16"
											title="Link to Business Customer Gateway's Home Page"
											alt="Image for Business Customer Gateway's Home Page link"
											height="20px" />
										</a>
									</div>
								</div>


								<!-- span class="navbar-brand mb-0 pt-4 mt-5" >Business Customer Gateway</span> -->
								<div class="row" style="float: right; margin-right: 3%;">
									<div class="col-12">
										<ul class="nav navbar-nav " id="navbar-display-name"
											style="float: right; padding-right: 0%;">
											<li style="padding-right: 20px;">
												<a href="https://gateway.usps.com/eAdmin/action/homepage" style="display: inline">
													<span class="navbar-text-blue"> Home </span> </a>
											</li>

											<li><span class="navbar-text-blue"> Hello
													FRANK!</span></li>

										</ul>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>


				<div class="container-fluid pt-0 mt-0 mb-0 pb-0"
					style="background-color: #F2F2F2; margin-top: 0px; padding-top: 0px;  display: none;">
					<div class="container">
						<div class="row">
							<div class="col-12">
								<nav class="navbar navbar-light bg-light navbar-expand-lg">
									<button type="button" class="navbar-toggle"
										data-toggle="collapse"
										data-target=".bs-example-navbar-collapse-1">
										<span class="sr-only">Toggle navigation</span> <span
											class="icon-bar"></span> <span class="icon-bar"></span> <span
											class="icon-bar"></span>
									</button>



									<!-- Collect the nav links, forms, and other content for toggling -->
									<div
										class="nav collapse bs-example-navbar-collapse-1 navbar-collapse py-0"
										style="margin-top: 0px; padding-top: 0px; horizontal-align: top; margin-left: 1.2%; position: relative;">

										<ul class="nav navbar-nav py-0 px-0"
											style="height: 25px; margin-top: 0px; padding-top: 0px;">
											<!-- begin mailing  -->
											<li><a tabindex="18" title="Link to Mailing Services"
												alt="Link to Mailing Services" class="menu-main-header"
												href="https://gateway.usps.com/eAdmin/action/addservice/getServiceTab?tabID=2">Mailing
													Services</a></li>
											<!-- begin shipping -->
											<li class="navbar-right-left"><a tabindex="19"
												title="Link to Shipping Services"
												alt="Link to Shipping Services" class="menu-main-header"
												href="https://gateway.usps.com/eAdmin/action/addservice/getServiceTab?tabID=1">Shipping
													Services</a></li>
											<li class="navbar-right-left"><a tabindex="20"
												title="Link to HCR Services" alt="Link to HCR Services"
												class="menu-main-header"
												href="https://gateway.usps.com/eAdmin/action/addservice/getServiceTab?tabID=5">HCR
													Services</a></li>

											<!-- begin additional tools  -->
											<li class="navbar-right-left"><a tabindex="21"
												title="Link to Additional Services"
												alt="Link to Additional Services" class="menu-main-header"
												href="https://gateway.usps.com/eAdmin/action/addservice/getServiceTab?tabID=3">Additional
													Services </a></li>
											<!-- end additional tools  -->
										</ul>
										<!--  begin navbar right -->



										<ul class="nav navbar-nav  px-0"
											style="height:; margin-top: 0px; padding-top: 0px; margin-right: 0%; float: right; width: 50%">
											<li class="navbar-right-first-custom"><i
												class="material-icons headericons">&#xE001;</i> 
													<span title="!" alt="Alert icon" class="bcg_badge-header">!</span>

												 <a tabindex="22" title="Link to Alerts"
												alt="Link to Alerts" class="menu-main-header"
												href="https://gateway.usps.com/eAdmin/action/alerts">Alerts</a>
											</li>
											<li class="navbar-right-custom"><i
												class="material-icons headericons img-fluid">&#xE0E1;</i>  <a tabindex="23" title="Link to Pending Requests"
												alt="Link to Pending Requests" class="menu-main-header"
												href="https://gateway.usps.com/eAdmin/action/inbox">
													Pending Requests</a></li>
											<!--  begin manage account dropdown -->
											<li class="dropdown navbar-right-custom"><i
												class="material-icons manageAccount headericons img-fluid">&#xE8A6;</i>
											<div title="View Manage Account" class="menu-main-header"
													alt="View Manage Account"
													style="margin-left: 11px; margin-top: 4px; text-underline: none;"
													tabindex="23" data-toggle="dropdown"
													class="dropdown-toggle menu-second menu-main-header">
													Manage Account <b class="caret"></b>
												</div>
												<ul class="dropdown-menu ">

													<li><a tabindex="24" title="Link to Manage Profile"
														alt="Link to Manage Profile" class="menu-main-header"
														href="https://gateway.usps.com/eAdmin/action/preferences/editprofile">Manage
															Profile</a></li>

													<li><a tabindex="25" title="Link to Manage Favorites"
														alt="Link to Manage Favorites" class="menu-main-header"
														href="https://gateway.usps.com/eAdmin/action/preferences/editfavorites">Manage
															Favorites</a></li>

													<li><a tabindex="26" title="Link to Manage Services"
														alt="Link to Manage Services" class="menu-main-header"
														href="https://gateway.usps.com/eAdmin/action/manageservices">Manage
															Services</a></li>

													<li><a tabindex="27" title="Link to Manage Locations"
														alt="Link to Manage Locations" class="menu-main-header"
														href="https://gateway.usps.com/eAdmin/action/managelocations">Manage
															Locations</a></li>

													<li><a tabindex="28" title="Link to Manage Users"
														alt="Link to Manage Users" class="menu-main-header"
														href="https://gateway.usps.com/eAdmin/action/manageusers/">Manage
															Users</a></li>
													<li class="divider"></li>

													<li><a tabindex="29" title="Click to Logout"
														alt="Click to Logout" class="menu-main-header"
														href="https://gateway.usps.com/eAdmin/view/signin/logout">Log
															Out</a></li>
												</ul></li>

											<li class="navbar-right-custom-middle"><a tabindex="30"
												class="menu-main-header" title="Link to USPS.com"
												alt="Link to USPS.com" href="https://www.usps.com/">
													USPS.com </a></li>

											<li class="navbar-right-custom-last"><a tabindex="31"
												class="menu-main-header" title="Link to Help"
												class="menu-main-header" alt="Link to Help"
												href="https://gateway.usps.com/eAdmin/action/resources/support">
													Help</a></li>
										</ul>
									</div>
								</nav>
							</div>
							<!-- /.navbar-collapse -->

						</div>
					</div>
				</div>
			</nav>

		</div>

	


		<div id="main">
				
		<!-- TAB E content-->
		<form method="post" action="https://gateway.usps.com/eAdmin/action/addservice/getServiceTab" id="selectServicesForm">
			<input type="hidden" name="serviceId" id="serviceId" value="">
			<input type="hidden" name="command" id="command" value="">
			<input type="hidden" name="roleName" id="roleName" value="">
			<input name="tabID" type="hidden" value="5" />
			<div class="bootstrap-iso">

				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<h2 class="service-page-title" style="margin-top: 20px;margin-bottom: 20px;">Logistics Gateway</h2>
						</div>
					</div>
				</div>

				<div class="container-fluid service-page-area">
					<div class="container service-page-container">
						<div class="row">
							<div class="col-md-8 col-sm-7" style="margin-left: 15px;">
								
									
									
									
									
										<div class="hcsIcon left"
											alt="icon of white truck"></div>
									
								
								<h4 class="serviceHeader">Gateway to manage your transporation relationship with the US Postal Service.</h4>
								<h6 class="serviceHeader text-justify"
									style="font-weight: normal; padding-top: 10px;">Services below enable Highway Transportation Suppliers to access current transportation schedules, real-time monitoring of vehicles, adjudication of trip exceptions and performance dashboards.</h6>
							</div>
							<div class="col-md-3 text-right"
								style="float: right; margin-right: 15px; margin-top: 15px;">
								
									
									
									
									
										<img title="" width="232" height="150"
											src="https://gateway.usps.com/eAdmin/images/gui/hcs_image.png"
											alt="image of parked postal trucks">
									
								
							</div>
						</div>

<!-- FHH COMMENTED OUT - remove locations dropdown
						
						<div class="row">
							<div class="col-md-12" style="margin-left: 15px;">

								
									
										
									
									<h5 class="serviceHeader" style="margin-top: 0;">Your
										Locations:</h5>
									<select tabindex="34" name="cridBox" onchange="submit();" style="width:98%; word-wrap:break-word;" title="Your Locations" class="wrapped-select">
										<option value="ALL" selected="selected">All Locations</option>
										<option value="6587123">HARRINGTON SOFTWARE ASSOCIATES, INC. (6587123), 7431 WILSON RD, WARRENTON, VA 20186-7464</option><option value="3765389">MATERIALS CUSTOMER SERVICE (3765389), 500 SW GARY ORMSBY DR, TOPEKA, KS 66624-9996</option><option value="8974561">USPS - MAIL ENTRY (8974561), 475 LENFANT PLZ SW RM 3660, WASHINGTON, DC 20260-0004</option>
									</select>
								
							</div>
						</div>
-->
						<!-- Table include -->
						<div class="row">
							<div class="col-md-12" style="margin-left: 15px;">
								<div id="servicesTableId">
									
	

	<script>var ctx = "/"</script>
	<br>
	
		<!-- start OTHER SERVICES -->
		
		

			<!-- Go To Services box -->
			<!-- start  message --->
			<div class="messageServices request" id="a1284323">
				<div class="service-line box-shadow-services clearfix">
 					
 					<div class = "row">
 						<div class = "col-md-8 col-sm-8 service-font">
 							<img src="https://gateway.usps.com/eAdmin/images/gui/bkg/icons/plus-grey.png"
							id=0 tabindex="37"
							onclick="showHideDesc(0, ctx)" alt="image of plus symbol" style="cursor:pointer;">
							Freight Auction&nbsp;&nbsp; 
							
							<span class="smaller"> 
								<a href="#/" class="underline" tabindex="38"
									onclick="showHideDesc(0, ctx)" title="Click to learn more about Freight Auction"
									id="more0" alt="Click to learn more about Freight Auction">more info >
								</a> 
							</span>
 						</div>

 						<div class = "col-md-3 col-sm-3 text-right" style="margin-top: 5px;">
							
								
								
									<!-- begin Request Access button-->
									<a title="Go to Service" href="https://prodp1.usps.com/adminweb/view.htm?requestPage=P1BALANCEFEES" tabindex="39">
												<button class="btn btn-sm btn-primary service-button" alt="Go to Freight Auction service button" type="button">
													<span class="service-link">Go to Service</span> 
												</button>
											</a>								
								
 								
							
 						</div>
 					</div>
 					
 					<!-- Service description -->
 					<div class = "row">
	 					<div class="col-md-11 col-sm-11"> 
							<div class="text-justify" id="desc0" style="display: none; margin-left: 25px;">
								<p class="text" style="margin-left: 25px;">
									Suppliers have the ability to accept or decline transportation based on a set rate.
									
									
								</p>
							</div>
	 					</div>
					</div>
					<!-- end of Service description -->
					
				</div>
			</div>
 			
		

			<!-- Go To Services box -->
			<!-- start  message --->
			<div class="messageServices request" id="a1284324">
				<div class="service-line box-shadow-services clearfix">
 					
 					<div class = "row">
 						<div class = "col-md-8 col-sm-8 service-font">
 							<img src="https://gateway.usps.com/eAdmin/images/gui/bkg/icons/plus-grey.png"
							id=1 tabindex="46"
							onclick="showHideDesc(1, ctx)" alt="image of plus symbol" style="cursor:pointer;">
							Contract Services&nbsp;&nbsp; 
							
							<span class="smaller"> 
								<a href="#/" class="underline" tabindex="47"
									onclick="showHideDesc(1, ctx)" title="Click to learn more about services available to manage your contracts."
									id="more1" alt="Click to learn more about services available to manage your contracts.">more info >
								</a> 
							</span>
 						</div>

 						<div class = "col-md-3 col-sm-3 text-right" style="margin-top: 5px;">
							
								
								
									<!-- begin Request Access button-->
									<span class="hasHover"> 
										<a tabindex="49" id="Request Access" href="https://gateway.usps.com/eAdmin/action/manageservices/manageByService?securityID=1284324" title="Get Access" class="buttons"><button class="btn btn-sm btn-default service-button" type="button" alt="HCR Manifests Get Access button">
														<strong>Get Access</strong>
												</button></a>
									</span> 
								
								
 								
							
 						</div>
 					</div>
 					
 					<!-- Service description -->
 					<div class = "row">
	 					<div class="col-md-11 col-sm-11"> 
							<div class="text-justify" id="desc1" style="display: none; margin-left: 25px;">
								<p class="text"  style="margin-left: 25px;">
									Suppliers have the ability to manage their contractual relationship with the US Postal Service including manifests (schedule), invoice and payment status.
								</p>
							</div>
	 					</div>
					</div>
					<!-- end of Service description -->
					
				</div>
			</div>
 			
		

			<!-- TRANSPORTATION PROCUREMENT SERVICES-->
			<!-- start  message --->
			<div class="messageServices request" id="a1284325">
				<div class="service-line box-shadow-services clearfix">
 					
 					<div class = "row">
 						<div class = "col-md-8 col-sm-8 service-font">
 							<img src="https://gateway.usps.com/eAdmin/images/gui/bkg/icons/plus-grey.png"
							id=2 tabindex="55"
							onclick="showHideDesc(2, ctx)" alt="image of plus symbol" style="cursor:pointer;">
							Transportation Procurement Services&nbsp;&nbsp; 
							
							<span class="smaller"> 
								<a href="#/" class="underline" tabindex="56"
									onclick="showHideDesc(2, ctx)" title="Click to learn more about Transportation Procurement Services"
									id="more2" alt="Click to learn more about Transportation Procurement Services">more info >
								</a> 
							</span>
 						</div>

 						<div class = "col-md-3 col-sm-3 text-right" style="margin-top: 5px;">
									<!-- begin Request Access button-->
									<span class="hasHover"> 
										<a tabindex="58" id="Request Access" href="https://gateway.usps.com/eAdmin/action/manageservices/manageByService?securityID=1284325" title="Get Access" class="buttons"><button class="btn btn-sm btn-default service-button" type="button" alt="Transportation Procurement Services Get Access button">
														<strong>Get Access</strong>
												</button></a>
									</span> 
 						</div>
 					</div>
 					
 					<!-- Service description -->
 					<div class = "row">
	 					<div class="col-md-11 col-sm-11"> 
							<div class="text-justify" id="desc2" style="display: none; margin-left: 25px;">
								<p class="text" style="margin-left: 25px;">
									Supplier has the ability to manage Transportation Procurement Services here... (refine description)
								</p>
							</div>
	 					</div>
					</div>
					<!-- end of Service description -->
					
				</div>
			</div>
			<!-- END OF:  TRANSPORTATION PROCUREMENT SERVICES-->

			<!-- STAF -->
			<!-- start  message --->
			<div class="messageServices request" id="a1284325">
				<div class="service-line box-shadow-services clearfix">
 					
 					<div class = "row">
 						<div class = "col-md-8 col-sm-8 service-font">
 							<img src="https://gateway.usps.com/eAdmin/images/gui/bkg/icons/plus-grey.png"
							id=2 tabindex="55"
							onclick="showHideDesc(3, ctx)" alt="image of plus symbol" style="cursor:pointer;">
							Automated Forms (Surface Transportation Automated Forms)&nbsp;&nbsp; 
							
							<span class="smaller"> 
								<a href="#/" class="underline" tabindex="56"
									onclick="showHideDesc(3, ctx)" title="Click to learn more about . Automated Forms (Surface Transportation Automated Forms)"
									id="more2" alt="Click to learn more about . Automated Forms (Surface Transportation Automated Forms)">more info >
								</a> 
							</span>
 						</div>

 						<div class = "col-md-3 col-sm-3 text-right" style="margin-top: 5px;">
									<!-- begin Request Access button-->
									<span class="hasHover"> 
										<a tabindex="58" id="Request Access" href="https://gateway.usps.com/eAdmin/action/manageservices/manageByService?securityID=1284325" title="Get Access" class="buttons"><button class="btn btn-sm btn-default service-button" type="button" alt="Transportation Procurement Services Get Access button">
														<strong>Get Access</strong>
												</button></a>
									</span> 
 						</div>
 					</div>
 					
 					<!-- Service description -->
 					<div class = "row">
	 					<div class="col-md-11 col-sm-11"> 
							<div class="text-justify" id="desc2" style="display: none; margin-left: 25px;">
								<p class="text" style="margin-left: 25px;">
									Supplier has the ability to manage . Automated Forms (Surface Transportation Automated Forms) here... (refine description)
								</p>
							</div>
	 					</div>
					</div>
					<!-- end of Service description -->
					
				</div>
			</div>
			<!-- END OF:  STAF -->
		
			<!-- TRANSPORTATION VISIBILITY and PERFORMANCE -->
			<!-- start  message --->
			<div class="messageServices request" id="a1284325">
				<div class="service-line box-shadow-services clearfix">
 					
 					<div class = "row">
 						<div class = "col-md-8 col-sm-8 service-font">
 							<img src="https://gateway.usps.com/eAdmin/images/gui/bkg/icons/plus-grey.png"
							id=2 tabindex="55"
							onclick="showHideDesc(4, ctx)" alt="image of plus symbol" style="cursor:pointer;">
							Transportation Visibility &amp; Performance&nbsp;&nbsp; 
							
							<span class="smaller"> 
								<a href="#/" class="underline" tabindex="56"
									onclick="showHideDesc(4, ctx)" title="Click to learn more about Transportation Visibility &amp; Performance"
									id="more2" alt="Click to learn more about Transportation Visibility &amp; Performance">more info >
								</a> 
							</span>
 						</div>

 						<div class = "col-md-3 col-sm-3 text-right" style="margin-top: 5px;">
									<!-- begin Request Access button-->
									<span class="hasHover"> 
										<a tabindex="58" id="Request Access" href="https://gateway.usps.com/eAdmin/action/manageservices/manageByService?securityID=1284325" title="Get Access" class="buttons"><button class="btn btn-sm btn-default service-button" type="button" alt="Transportation Procurement Services Get Access button">
														<strong>Get Access</strong>
												</button></a>
									</span> 
 						</div>
 					</div>
 					
 					<!-- Service description -->
 					<div class = "row">
	 					<div class="col-md-11 col-sm-11"> 
							<div class="text-justify" id="desc2" style="display: none; margin-left: 25px;">
								<p class="text" style="margin-left: 25px;">
									Supplier has the ability to manage Transportation Visibility &amp; Performance here... (refine description)
								</p>
							</div>
	 					</div>
					</div>
					<!-- end of Service description -->
					
				</div>
			</div>
			<!-- END OF:  TRANSPORTATION VISIBILITY and PERFORMANCE -->


		<!-- end OTHER SERVICES -->
	

								</div>
							</div>
						</div>

						
					</div>
				</div>
			</div>

			<div class="dijitHidden">
				
	
<!-- FHH COMMENTED OUT ... remove location related detail 	
		<div id="become_bsa_popup" title="Warning Dialog"
			data-dojo-type="dijit/Dialog"
			style="width: 600px; height: auto; position: relative;text-align:center;">
			<h4 style="text-align:center;">No BSA For This Location</h4>
			 <br>
			<div align="center" style="text-align:center;" id="warningToBeReplaced">
			</div>
			<div align="center" style="text-align:center;">	
				You are the first person requesting access to this service for your Business Location. As such you will become the BSA responsible for controlling access to this service for this location. Do you agree?</div>
			
			<br>
			<div align="center" style="display: inline-block;text-align:center;">
					<div>
					<span class="requestButtonpri"> 
						<span class="hasHover">
							<input type="button" class="buttons"  style="text-align:center;width:266px;" title="Agree & Become BSA" alt="Agree Button"
							onclick="yesClickHandler('ADMIN');" name="Agree & Become BSA" id="YES" value="Agree & Become BSA" tabindex="1001" /> 
						</span> 
					</span>
					<span class="requestButtonsnd"> 
						<span class="hasHover"> <input type="button" class="buttons" style="margin-left: 15px;text-align:center;width:180px;"
							onclick="yesClickHandler('USER');" value="Decline" name="NO" id="NO" title="Decline" alt="Decline button" tabindex="1002" /> 
						</span>
					</span>
				</div>
			</div>
			
		</div>
-->	

			</div>
		<div style="display: none;"><input type="hidden" name="_sourcePage" value="6Gats09WA7E09gmaQyWl1kVkq0yXTIF2RU_pdq80UJ319uf92GkEVovPntwdcYvs1U0HS0_vKuo=" /><input type="hidden" name="__fp" value="r_clNIa3jsvuuSoZ7ddKpw==" /></div></form>
		<script
			src="https://gateway.usps.com/eAdmin/scripts/additionalservices/otherServices.js"></script>
	
		</div>
		<!-- end page-section-->

		<!-- end #main-inner -->

		
		<!-- End #page -->
	</div>
	<!-- Begin Footer -->
		<div id="footer" class="footer">
			<div class="section">
				<!-- Begin Footer -->
				
	
		<!-- Begin Footer -->

<!--  FHH COMMENTED OUT
<span class="hide-fromsighted">Begin Footer</span>
-->

<!--  FHH ... set display: none for now on footer for wirefream -->
<div class="bootstrap-iso main-footer" style="display: none;">
		<div id="usps-footer" class="container" >
			<div class="row" id="footer-margin-row">
			 
			 	<div class="col-md-12">
						<div class="row" id="usps-footer-links">
						
									<div class="col-md-2 footer-link">
		
										<h3>LEGAL</h3>
										<a
												href="http://about.usps.com/who-we-are/privacy-policy/privacy-policy-highlights.htm"
												tabindex="9500" title="Link to Privacy Policy" alt="Link to Privacy Policy">Privacy Policy
													</a><br>
											<a href="http://about.usps.com/termsofuse.htm"
												tabindex="9501" title="Link to Terms of Use" alt="Link to Terms of Use">Terms of Use </a><br>
											
											<a
												href="http://about.usps.com/who-we-are/foia/welcome.htm"
												tabindex="9502" title="Link to FOIA" alt="Link to FOIA">FOIA </a><br>
											<a
												href="http://about.usps.com/who-we-are/no-fear-act/welcome.htm"
												tabindex="9503" title="Link to No FEAR Act EEO Data" alt="Link to No FEAR Act EEO Data">No FEAR Act
													EEO Data </a>
									</div>
									<div class="col-md-1">&nbsp;</div>
									<div class="col-md-2 footer-link">
										<h3>ON USPS.COM</h3>
										<a
												href="http://www.usps.com/gov-services/gov-services.htm"
												tabindex="9504" title="Link to Government Services" alt="Link to Government Services">Government
													Services </a><br>
											<a href="https://www.usps.com/shop" tabindex="9505"
												title="Link to Buy Stamps & Shop" alt="Link to Buy Stamps & Shop">Buy Stamps &amp; Shop </a><br>
											<a href="http://www.usps.com/shipping/label.htm"
												tabindex="9506" title="Link to Print a Label with Postage" alt="Link to Print a Label with Postage">Print a
													Label with Postage </a><br>
											<a
												href="http://www.usps.com/customer-service/customer-service.htm"
												tabindex="9507" title="Link to Customer Service" alt="Link to Customer Service">Customer Service
													</a><br>
											<a href="http://www.usps.com/globals/site-index.htm"
												tabindex="9508" title="Link to Site Index" alt="Link to Site Index">Site Index </a>
									</div>
									<div class="col-md-1">&nbsp;</div>
									<div class="col-md-2 footer-link">
										<h3>ON ABOUT.USPS.COM</h3>
											<a href="http://about.usps.com" tabindex="9509"
												title="Link to know About USPS Home" alt="Link to know About USPS Home">About USPS Home </a><br>
											<a href="http://about.usps.com/news/welcome.htm"
												tabindex="9510" title="Link to Newsroom" alt="Link to Newsroom">Newsroom </a><br>
											<a
												href="http://about.usps.com/news/service-alerts/welcome.htm"
												tabindex="9511" title="Link to Mail Service Updates" alt="Link to Mail Service Updates">Mail Service
													Updates </a><br>
											<a
												href="http://about.usps.com/forms-publications/welcome.htm"
												tabindex="9512" title="Link to Forms and Publications" alt="Link to Forms and Publications">Forms &amp;
													Publications </a><br>
											<a href="http://about.usps.com/careers/welcome.htm"
												tabindex="9513" title="Link to Careers" alt="Link to Careers">Careers </a>
										
									</div>
									<div class="col-md-1">&nbsp;</div>
									<div class="col-md-2 footer-link">
										<h3>OTHER USPS SITES</h3>
										<a href="https://gateway.usps.com" tabindex="9514"
												title="Link to Business Customer Gateway" alt="Link to Business Customer Gateway">Business Customer
													Gateway </a><br>
											<a href="https://postalinspectors.uspis.gov/"
												tabindex="9515" title="Link to Postal Inspectors" alt="Link to Postal Inspectors">Postal Inspectors
													</a><br>
											<a href="http://www.uspsoig.gov/" tabindex="9516"
												title="Link to Inspector General" alt="Link to Inspector General">Inspector General </a><br>
											<a href="http://pe.usps.com/" tabindex="9517"
												title="Link to Postal Explorer" alt="Link to Postal Explorer">Postal Explorer </a>
										
							</div>
						</div>
					</div>
					</div>
				<br>
						<div class="row">
							<div class="col-md-12">
								<div id="footer-copyright">
									<div id="usps-footer-copyright" style="display: inline;">
											Copyright &copy; <script type="text/javascript">
											var theDate = new Date();
											document.write(theDate.getFullYear());
											</script> USPS. All Rights Reserved.
									</div>
								</div>
							</div>
						</div>
			</div>
</div>
		<link rel="stylesheet" href="https://gateway.usps.com/eAdmin/styles/footer.css" type="text/css" media="all" />
		<!-- End footer -->
<!-- FHH COMMENTED OUT
<script type="text/javascript" src="https://gateway.usps.com:443https://gateway.usps.com/eAdmin/scripts/support.js"></script>
-->	

				<!-- End footer -->
			</div>
		</div>
	<div class="dijitHidden">
		
<!--  FHH ... set display: none for now on footer for wireframe -->	
		<div id="timeOutDialogId" title="Warning:" data-dojo-type="dijit/Dialog" class="left clearfix"  style="display: none;">
			<div class="bootstrap-iso">
				<div class = "reviewRequestNote margin-bottom-30" style="">Your current BCG session will be logged out in one minute due to inactivity</div>
				<div class = "modal-buttons-div">
					<span class="hasHover"> 
						<a tabindex="1005" href="#" title="OK" class="btn btn-sm btn-primary" id="TimeOutCloseButtonId">OK</a>
					</span>	
				</div>			
			</div>
		</div>
	

	</div>

	 <!-- Bootstrap -->
	 <script src="https://gateway.usps.com/eAdmin/scripts/bootstrap/bootstrap.min.js"></script>
	 <script src="https://gateway.usps.com/eAdmin/scripts/timeout/timeout.js"></script>
</body>
	</html>
)
