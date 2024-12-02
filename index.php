<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apple-Style Simplified</title>
    <style>
        /* Global Styles */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            color: #333;
            background-color: #f5f5f7;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: "San Francisco", "Helvetica Neue", Arial, sans-serif;
            font-weight: 600;
            margin: 0;
        }

        .navbar {
            background-color: #ffffff;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #e0e0e0;
        }

        .navbar a {
            font-size: 16px;
            margin: 0 15px;
            text-decoration: none;
            color: #0071e3;
        }

        .header {
            text-align: center;
            padding: 100px 20px;
            background: linear-gradient(to bottom, #f5f5f7, #e0e0e0);
        }

        .header h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .section {
            margin-bottom: 60px;
        }

        .section h2 {
            font-size: 32px;
            margin-bottom: 20px;
        }

        .section p {
            font-size: 18px;
            line-height: 1.6;
            color: #6e6e73;
        }

        .footer {
            text-align: center;
            padding: 20px 0;
            background-color: #f5f5f7;
            color: #6e6e73;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </div>

    <!-- Header -->
    <header class="header" id="home">
        <h1>Welcome to Apple-Style Site</h1>
    </header>

    <!-- Main Content -->
    <div class="content">
        <!-- Section 1 -->
        <div class="section" id="about">
            <h2>About Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel nisi ac quam fermentum aliquet. Donec tincidunt, libero id blandit suscipit, felis purus tincidunt lorem, nec tincidunt nisi arcu non ante.</p>
        </div>

        <!-- Section 2 -->
        <div class="section" id="services">
            <h2>Our Services</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent malesuada ligula vel quam vulputate, ac sagittis justo hendrerit.</p>
        </div>

        <!-- Section 3 -->
        <div class="section" id="contact">
            <h2>Contact Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vehicula, eros non scelerisque fermentum, est lorem pellentesque velit, at luctus nunc nulla a purus.</p>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2024 Your Website. All rights reserved.</p>
    </footer>
</body>
</html>
