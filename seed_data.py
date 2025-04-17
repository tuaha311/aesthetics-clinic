import os
import django
import random
from django.utils.text import slugify

# Set up Django environment first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()

# Now import Django models after settings are configured
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from azfi.models import (
    Treatment, TreatmentFAQ, BeforeAfterImage, 
    TeamMember, Testimonial, BlogPost
)

def clean_database():
    """Remove all existing records to start fresh"""
    print("Cleaning database...")
    Treatment.objects.all().delete()
    TeamMember.objects.all().delete()
    Testimonial.objects.all().delete()
    BlogPost.objects.all().delete()
    print("Database cleaned.")

def create_sample_treatments():
    """Create sample treatments with FAQs"""
    print("Creating treatments...")
    
    # Face Treatments
    treatments = [
        {
            'name': 'Microneedling',
            'category': 'FACE',
            'description': 'Microneedling is a minimally invasive cosmetic procedure that involves using fine needles to create tiny punctures in the skin. This triggers the body\'s wound healing process, resulting in increased collagen and elastin production, which can improve skin texture, reduce scarring, and rejuvenate the skin.',
            'what_to_expect': 'During your microneedling treatment, a topical anesthetic will be applied to minimize discomfort. The procedure takes approximately 30-45 minutes. You may experience mild redness and sensitivity for 1-3 days following treatment. For optimal results, we recommend a series of 3-6 treatments spaced 4-6 weeks apart.',
            'price_range': '$250 - $350',
            'duration': '45 minutes',
            'featured': True,
            'faqs': [
                {'question': 'Is microneedling painful?', 'answer': 'We apply a topical numbing cream before the procedure, so most patients experience minimal discomfort. You may feel a slight prickling sensation during treatment.'},
                {'question': 'How many sessions will I need?', 'answer': 'For optimal results, we recommend a series of 3-6 treatments spaced 4-6 weeks apart, depending on your specific skin concerns.'},
                {'question': 'What is the recovery time?', 'answer': 'Most patients experience mild redness and sensitivity for 1-3 days following treatment. You can typically resume normal activities the next day.'}
            ]
        },
        {
            'name': 'Chemical Peel',
            'category': 'FACE',
            'description': 'Chemical peels are facial treatments that use a chemical solution to remove the top layers of skin, revealing smoother, more evenly toned skin underneath. They can address various skin concerns including fine lines, sun damage, acne scars, and hyperpigmentation.',
            'what_to_expect': 'During your chemical peel, the solution will be applied to your cleansed skin and left on for a specific amount of time before being neutralized. You may feel a tingling or warm sensation during application. Depending on the depth of the peel, recovery time ranges from 1-14 days, during which you may experience redness, peeling, and sensitivity.',
            'price_range': '$150 - $400',
            'duration': '30 minutes',
            'featured': False,
            'faqs': [
                {'question': 'What types of chemical peels do you offer?', 'answer': 'We offer superficial (lunchtime), medium, and deep peels. The type recommended for you will depend on your skin concerns and desired results.'},
                {'question': 'How often can I get a chemical peel?', 'answer': 'Superficial peels can be done every 2-4 weeks, medium peels every 3-6 months, and deep peels typically only once.'},
                {'question': 'Will my skin actually peel?', 'answer': 'Yes, most patients experience some degree of peeling following a chemical peel. The extent of peeling depends on the strength of the peel.'}
            ]
        },
        {
            'name': 'HydraFacial',
            'category': 'FACE',
            'description': 'HydraFacial is a multi-step treatment that cleanses, exfoliates, and extracts impurities while simultaneously hydrating the skin with antioxidants, peptides, and hyaluronic acid. This non-invasive procedure is suitable for all skin types and addresses multiple skin concerns with no downtime.',
            'what_to_expect': 'The HydraFacial treatment takes about 30 minutes and includes cleansing and exfoliation, a gentle acid peel, painless extractions, and hydration with antioxidants and hyaluronic acid. The procedure is painless with no downtime, and you\'ll see immediate results in skin hydration, tone, and texture.',
            'price_range': '$180 - $300',
            'duration': '30 minutes',
            'featured': True,
            'faqs': [
                {'question': 'How long do the results last?', 'answer': 'Many clients report visible skin refinement and an even, radiant skin tone after just one treatment. The smooth results and hydration may last 5-7 days or longer.'},
                {'question': 'How often should I get a HydraFacial?', 'answer': 'For optimal results, we recommend a HydraFacial once every 4 weeks.'},
                {'question': 'Is there any downtime after a HydraFacial?', 'answer': 'There is no downtime with HydraFacial treatments. You can resume normal activities immediately after treatment.'}
            ]
        },
    ]
    
    # Body Treatments
    body_treatments = [
        {
            'name': 'Body Contouring',
            'category': 'BODY',
            'description': 'Our non-surgical body contouring treatments use advanced technology to target and reduce stubborn fat pockets, tighten skin, and shape your body. These treatments are ideal for those who maintain a healthy lifestyle but struggle with areas resistant to diet and exercise.',
            'what_to_expect': 'During your body contouring session, you\'ll relax while our specialist applies the device to the targeted treatment areas. Most treatments feel like a warming sensation or gentle suction. Sessions typically last 30-60 minutes depending on the area being treated. Most clients require a series of treatments for optimal results.',
            'price_range': '$300 - $500 per session',
            'duration': '60 minutes',
            'featured': True,
            'faqs': [
                {'question': 'Is body contouring painful?', 'answer': 'Most clients report minimal discomfort during body contouring treatments. You may feel a warming sensation, gentle suction, or mild tingling depending on the specific technology used.'},
                {'question': 'How many sessions will I need?', 'answer': 'Most clients require 4-8 sessions spaced 1-2 weeks apart for optimal results.'},
                {'question': 'Is there any downtime?', 'answer': 'There is minimal to no downtime with our body contouring treatments. You may experience mild redness or sensitivity in the treated area, but this typically resolves within a few hours.'}
            ]
        },
        {
            'name': 'Laser Hair Removal',
            'category': 'BODY',
            'description': 'Our laser hair removal treatments use advanced laser technology to target and destroy hair follicles, resulting in permanent hair reduction. This popular treatment is effective for various skin types and can be performed on virtually any area of the body.',
            'what_to_expect': 'During treatment, you\'ll feel a sensation similar to a rubber band snap as the laser targets each hair follicle. Sessions vary in length depending on the treatment area, ranging from 15 minutes for small areas to 60+ minutes for larger areas. For optimal results, we recommend a series of 6-8 treatments spaced 4-6 weeks apart.',
            'price_range': '$150 - $600 per session',
            'duration': '15-60 minutes',
            'featured': False,
            'faqs': [
                {'question': 'Does laser hair removal hurt?', 'answer': 'Most clients describe the sensation as similar to a rubber band snap against the skin. We use cooling technology to minimize discomfort during treatment.'},
                {'question': 'How many sessions will I need?', 'answer': 'Most clients require 6-8 treatments spaced 4-6 weeks apart for optimal results. Maintenance sessions may be needed once or twice a year.'},
                {'question': 'Which areas can be treated?', 'answer': 'Laser hair removal can be performed on virtually any area of the body, including face, underarms, legs, bikini area, back, and chest.'}
            ]
        },
    ]
    
    # Injectable Treatments
    injectable_treatments = [
        {
            'name': 'Anti-Wrinkle Injections',
            'category': 'INJECTABLES',
            'description': 'Our anti-wrinkle injections temporarily relax facial muscles that cause expression lines and wrinkles, resulting in smoother, younger-looking skin. This quick, minimally invasive treatment is ideal for treating forehead lines, crow\'s feet, and frown lines.',
            'what_to_expect': 'After a consultation to discuss your goals, your provider will administer a series of small injections into the targeted muscles. The procedure takes about 15-20 minutes with minimal discomfort. Results typically appear within 3-7 days and last 3-4 months. There\'s minimal downtime, though you may experience slight bruising or swelling at injection sites.',
            'price_range': '$250 - $600',
            'duration': '20 minutes',
            'featured': True,
            'faqs': [
                {'question': 'When will I see results?', 'answer': 'Results typically begin to appear within 3-7 days after treatment, with full results visible after 2 weeks.'},
                {'question': 'How long do results last?', 'answer': 'Results typically last 3-4 months for most patients. Regular treatments every 3-4 months maintain optimal results.'},
                {'question': 'Are there any side effects?', 'answer': 'Common side effects include temporary bruising, redness, or swelling at injection sites. These typically resolve within a few days.'}
            ]
        },
        {
            'name': 'Dermal Fillers',
            'category': 'INJECTABLES',
            'description': 'Dermal fillers are injectable treatments that restore volume, smooth lines, and enhance facial contours. Our range of premium fillers can address various concerns including nasolabial folds, marionette lines, lip enhancement, cheek volume, and jawline definition.',
            'what_to_expect': 'After a consultation to discuss your goals, your provider will administer the filler using a fine needle or cannula. A topical numbing cream can be applied for comfort. The procedure takes 30-45 minutes, with results visible immediately and lasting 6-24 months depending on the filler type and treatment area.',
            'price_range': '$500 - $1200',
            'duration': '45 minutes',
            'featured': False,
            'faqs': [
                {'question': 'What types of fillers do you use?', 'answer': 'We use premium hyaluronic acid fillers from trusted brands. The specific filler recommended will depend on your treatment area and desired results.'},
                {'question': 'Do filler injections hurt?', 'answer': 'We use topical numbing cream and fillers containing lidocaine to minimize discomfort during treatment.'},
                {'question': 'How long do fillers last?', 'answer': 'Results typically last 6-24 months depending on the filler type, treatment area, and individual factors.'}
            ]
        },
    ]
    
    # Add all treatments to the list
    treatments.extend(body_treatments)
    treatments.extend(injectable_treatments)
    
    # Create the treatments in the database
    created_treatments = []
    for t in treatments:
        faqs = t.pop('faqs')
        treatment = Treatment.objects.create(
            name=t['name'],
            slug=slugify(t['name']),
            description=t['description'],
            what_to_expect=t['what_to_expect'],
            price_range=t['price_range'],
            duration=t['duration'],
            category=t['category'],
            featured=t['featured'],
            # You would need actual image files here
            image="treatments/placeholder.jpg"
        )
        
        # Create FAQs for this treatment
        for i, faq in enumerate(faqs):
            TreatmentFAQ.objects.create(
                treatment=treatment,
                question=faq['question'],
                answer=faq['answer'],
                order=i
            )
        
        created_treatments.append(treatment)
        print(f"Created treatment: {t['name']}")
    
    return created_treatments

def create_team_members():
    """Create sample team members"""
    print("Creating team members...")
    
    team_members = [
        {
            'name': 'Dr. Sophia Williams',
            'role': 'Lead Aesthetician & Medical Director',
            'bio': 'Dr. Williams has over 15 years of experience in aesthetic medicine. Board-certified in dermatology, she specializes in advanced injectable treatments and has trained practitioners across the country. Her philosophy emphasizes natural-looking results that enhance each client\'s unique beauty.',
            'order': 1
        },
        {
            'name': 'Emma Johnson',
            'role': 'Senior Aesthetician',
            'bio': 'With 10 years in the industry, Emma specializes in advanced facial treatments and chemical peels. Her knowledge of skincare products and ingredients allows her to create personalized treatment plans that deliver exceptional results. Clients love her gentle touch and thorough approach.',
            'order': 2
        },
        {
            'name': 'Michael Chen',
            'role': 'Body Contouring Specialist',
            'bio': 'Michael brings 8 years of experience in non-surgical body contouring treatments. His extensive training with cutting-edge technologies and precise technique ensure optimal results. He takes pride in helping clients achieve their body goals and boost their confidence.',
            'order': 3
        },
        {
            'name': 'Jessica Martinez',
            'role': 'Laser Technician & Skincare Specialist',
            'bio': 'Jessica specializes in laser treatments for hair removal, skin rejuvenation, and pigmentation. Certified in multiple laser platforms, she has 6 years of experience delivering safe, effective treatments for all skin types. Her detailed assessments ensure each client receives the most appropriate treatment plan.',
            'order': 4
        }
    ]
    
    created_members = []
    for tm in team_members:
        member = TeamMember.objects.create(
            name=tm['name'],
            role=tm['role'],
            bio=tm['bio'],
            order=tm['order'],
            # You would need actual image files here
            image="team/placeholder.jpg"
        )
        created_members.append(member)
        print(f"Created team member: {tm['name']}")
    
    return created_members

def create_testimonials(treatments):
    """Create sample testimonials"""
    print("Creating testimonials...")
    
    testimonials = [
        {
            'name': 'Sarah T.',
            'quote': "I've tried many facial treatments over the years, but the HydraFacial at Aesthetics Clinic is truly exceptional. My skin looked radiant immediately after the first treatment, and the results just keep getting better. The staff is knowledgeable and made me feel completely comfortable.",
            'treatment_name': 'HydraFacial',
            'featured': True
        },
        {
            'name': 'James K.',
            'quote': "After years of being self-conscious about my forehead lines, I finally decided to try anti-wrinkle injections. Dr. Williams was amazing - she explained everything clearly and the results look so natural. No one can tell I've had anything done, they just think I look well-rested!",
            'treatment_name': 'Anti-Wrinkle Injections',
            'featured': True
        },
        {
            'name': 'Michelle D.',
            'quote': "The body contouring treatments have made such a difference to my abdomen after having children. The staff was supportive throughout my treatment journey, and I'm thrilled with the results. I finally feel confident in my clothes again!",
            'treatment_name': 'Body Contouring',
            'featured': True
        },
        {
            'name': 'David L.',
            'quote': 'I was nervous about getting microneedling but the team put me at ease. The improvement in my acne scars after just three sessions is remarkable. The entire experience from consultation to treatment was professional and exceeded my expectations.',
            'treatment_name': 'Microneedling',
            'featured': False
        },
        {
            'name': 'Amara J.',
            'quote': 'My experience with laser hair removal has been life-changing. After years of struggling with ingrown hairs from shaving, I finally have smooth, clear skin. The treatments were much more comfortable than I expected, and the results are permanent!',
            'treatment_name': 'Laser Hair Removal',
            'featured': False
        },
        {
            'name': 'Robert P.',
            'quote': "I was hesitant about trying dermal fillers, but I'm so glad I did. The treatment restored volume to my cheeks and smoothed out my nasolabial folds, taking years off my appearance. The results look completely natural, which was very important to me.",
            'treatment_name': 'Dermal Fillers',
            'featured': True
        }
    ]
    
    created_testimonials = []
    for t in testimonials:
        # Find the corresponding treatment
        treatment = None
        for tr in treatments:
            if tr.name == t['treatment_name']:
                treatment = tr
                break
        
        testimonial = Testimonial.objects.create(
            name=t['name'],
            quote=t['quote'],
            treatment=treatment,
            featured=t['featured'],
            # You would need actual image files here
            image=None
        )
        created_testimonials.append(testimonial)
        print(f"Created testimonial from: {t['name']}")
    
    return created_testimonials

def create_blog_posts():
    """Create sample blog posts"""
    print("Creating blog posts...")
    
    # Ensure we have a user for the blog author
    try:
        author = User.objects.get(username='admin')
    except User.DoesNotExist:
        author = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    
    posts = [
        {
            'title': 'Understanding the Different Types of Chemical Peels',
            'content': """
            Chemical peels are popular skin treatments that can address various skin concerns including fine lines, sun damage, uneven skin tone, and acne scars. But with so many different types available, how do you know which one is right for you?

            **Superficial Peels**

            Also known as lunchtime peels, these use mild acids like alpha-hydroxy acid to gently exfoliate the outermost layer of the skin. They're ideal for addressing minor skin concerns and improving overall skin brightness and texture with minimal downtime.

            **Medium Peels**

            Medium peels penetrate the skin more deeply, reaching the middle layers of the skin. They typically use trichloroacetic acid (TCA) or glycolic acid and are effective for treating wrinkles, acne scars, and uneven skin tone. Recovery time is typically 5-7 days.

            **Deep Peels**

            Deep peels use phenol to penetrate the lower dermal layer of the skin. They can dramatically improve the appearance of deeper wrinkles, scars, and even precancerous growths. Recovery can take 2-3 weeks, and results can last for years.

            **Which Peel is Right for You?**

            The best chemical peel for you depends on your skin concerns, skin type, and how much downtime you can accommodate. During a consultation, our skincare experts will evaluate your skin and recommend the most appropriate treatment to help you achieve your skin goals.

            Remember, proper sun protection is essential following any chemical peel treatment, as your skin will be more sensitive to UV damage.
            """,
            'excerpt': 'Learn about different types of chemical peels, from superficial to deep, and how to choose the right one for your skin concerns.'
        },
        {
            'title': 'The Science Behind Collagen Stimulating Treatments',
            'content': """
            Collagen is the most abundant protein in our bodies and is essential for maintaining skin elasticity, firmness, and a youthful appearance. As we age, our natural collagen production decreases, leading to wrinkles, sagging skin, and other signs of aging. Fortunately, several aesthetic treatments can stimulate collagen production to help restore more youthful skin.

            **Microneedling**

            Microneedling works by creating thousands of microscopic channels in the skin with tiny needles. These micro-injuries trigger the body's wound healing response, which includes collagen and elastin production. Studies have shown that microneedling can increase collagen production by up to 400% with multiple treatments.

            **Radiofrequency Treatments**

            Radiofrequency devices heat the deeper layers of the skin to temperatures that trigger collagen contraction and stimulate new collagen formation. This heating process activates fibroblasts, the cells responsible for collagen production, without damaging the skin's surface.

            **Laser Treatments**

            Certain laser treatments, particularly fractional lasers, create controlled micro-injuries in the skin that stimulate collagen remodeling. Different wavelengths target specific skin concerns, from fine lines to deeper wrinkles or scars.

            **Platelet-Rich Plasma (PRP)**

            PRP treatments use growth factors from your own blood to stimulate collagen production. These growth factors activate fibroblasts and accelerate tissue regeneration when injected into or applied to the skin.

            **The Timeline for Results**

            While some treatments provide immediate effects through tissue tightening, the more significant results from collagen stimulation develop gradually. New collagen formation typically begins 4-8 weeks after treatment and continues to improve over 3-6 months. Multiple treatment sessions are usually recommended for optimal results.

            Understanding the science behind collagen stimulation helps explain why patience and consistency are key when undergoing these treatments. The investment in stimulating your body's natural collagen production can provide longer-lasting rejuvenation than treatments that offer only temporary results.
            """,
            'excerpt': 'Discover how treatments like microneedling, radiofrequency, and lasers stimulate collagen production to combat aging and improve skin quality.'
        },
        {
            'title': 'Choosing Between Anti-Wrinkle Injections and Dermal Fillers',
            'content': """
            Injectable treatments are among the most popular non-surgical cosmetic procedures today, with anti-wrinkle injections and dermal fillers leading the way. While both can reduce signs of aging, they work in very different ways and address different concerns. Understanding these differences is key to achieving your desired results.

            **How Anti-Wrinkle Injections Work**

            Anti-wrinkle injections use a purified protein to temporarily relax the facial muscles that cause dynamic wrinkles—those that appear with facial expressions like smiling, frowning, or squinting. By reducing muscle activity, these injections smooth out expression lines, particularly on the forehead, between the brows, and around the eyes.

            **How Dermal Fillers Work**

            Dermal fillers, typically made from hyaluronic acid (a substance naturally found in the body), work by restoring lost volume and filling in static wrinkles—those visible when your face is at rest. Fillers can plump thin lips, enhance shallow contours, soften facial creases, and improve the appearance of recessed scars.

            **Which Concerns Do They Address?**

            Anti-wrinkle injections are ideal for:
            - Forehead lines
            - Frown lines between the brows
            - Crow's feet around the eyes
            - Bunny lines on the nose
            - Dimpled chin
            - Neck bands

            Dermal fillers are better for:
            - Nasolabial folds (smile lines)
            - Marionette lines (lines from corners of the mouth to chin)
            - Loss of volume in cheeks or temples
            - Lip enhancement
            - Jawline definition
            - Under-eye hollows

            **Combining Treatments**

            Many clients benefit from combining both treatments for what's often called a "liquid facelift." For example, anti-wrinkle injections might be used on the upper face while fillers restore volume in the mid and lower face.

            **Longevity of Results**

            Anti-wrinkle injections typically last 3-4 months, while dermal fillers can last anywhere from 6-24 months depending on the product used and treatment area.

            During your consultation, our medical professionals will assess your facial anatomy, discuss your concerns, and recommend the most appropriate treatment or combination of treatments to help you achieve natural-looking results.
            """,
            'excerpt': 'Understand the differences between anti-wrinkle injections and dermal fillers to determine which injectable treatment is right for your aesthetic goals.'
        }
    ]
    
    created_posts = []
    for p in posts:
        post = BlogPost.objects.create(
            title=p['title'],
            slug=slugify(p['title']),
            content=p['content'],
            excerpt=p['excerpt'],
            author=author,
            # You would need actual image files here
            featured_image="blog/placeholder.jpg"
        )
        created_posts.append(post)
        print(f"Created blog post: {p['title']}")
    
    return created_posts

if __name__ == '__main__':
    clean_database()
    treatments = create_sample_treatments()
    team_members = create_team_members()
    testimonials = create_testimonials(treatments)
    blog_posts = create_blog_posts()
    
    print("\nSeed data creation complete!")
    print(f"Created {len(treatments)} treatments")
    print(f"Created {len(team_members)} team members")
    print(f"Created {len(testimonials)} testimonials")
    print(f"Created {len(blog_posts)} blog posts")
    print("\nNote: You will need to add actual images through the admin interface.") 