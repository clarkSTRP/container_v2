<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Website</title>
    <style>
        /* Global Styles */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            color: #333;
            background-color: #f5f5f7;
        }

        h1, h2 {
            font-family: "San Francisco", "Helvetica Neue", Arial, sans-serif;
            font-weight: 600;
            margin: 0;
        }

        h1 {
            font-size: 36px;
        }

        h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }

        p {
            font-size: 14px;
            line-height: 1.4;
            color: #6e6e73;
            margin: 5px 0;
        }

        .navbar {
            background-color: #ffffff;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #e0e0e0;
        }

        .navbar a {
            font-size: 14px;
            margin: 0 10px;
            text-decoration: none;
            color: #0071e3;
        }

        .header {
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(to bottom, #f5f5f7, #e0e0e0);
        }

        .header h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }

        .content {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px 15px;
        }

        .section {
            margin-bottom: 40px;
        }

        .section h2 {
            font-size: 20px;
        }

        .footer {
            text-align: center;
            padding: 10px 0;
            background-color: #f5f5f7;
            color: #6e6e73;
            font-size: 12px;
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
        <h1>test website</h1>
        <p>test test</p>
    </header>

    <!-- Main Content -->
    <div class="content">
        <!-- SQL Connection Section -->
        <div class="section">
            <h2>Database Connection</h2>
            <p>
                <?php
                $host = getenv('MYSQL_HOST');
                $db = getenv('MYSQL_DATABASE');
                $user = getenv('MYSQL_USER');
                $pass = getenv('MYSQL_PASSWORD');

                try {
                    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
                    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                    echo "Connected to the database successfully!";
                } catch (PDOException $e) {
                    echo "Connection failed: " . $e->getMessage();
                }
                ?>
            </p>
        </div>

        <!-- About Section -->
        <div class="section" id="about">
            <h2>About Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vel nisi ac quam fermentum aliquet. Donec tincidunt, libero id blandit suscipit, felis purus tincidunt lorem.</p>
        </div>

        <!-- Services Section -->
        <div class="section" id="services">
            <h2>Our Services</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent malesuada ligula vel quam vulputate, ac sagittis justo hendrerit.</p>
        </div>

        <!-- Contact Section -->
        <div class="section" id="contact">
            <h2>Contact Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            <form action="/action_page.php" method="post">
                <p><input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; font-size: 14px;"></p>
                <p><input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; font-size: 14px;"></p>
                <p><textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 8px; font-size: 14px; height: 80px;"></textarea></p>
                <p><button type="submit" style="padding: 8px 16px; font-size: 14px; background-color: #0071e3; color: #ffffff; border: none; cursor: pointer;">Send</button></p>
            </form>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2024 Your Website. All rights reserved.</p>
    </footer>
</body>
</html>
